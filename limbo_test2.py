#!/usr/bin/env python3

import csv
import subprocess
import os
import yaml

# --- Configuration ---
# Path to the CSV file
CSV_FILE = "issues.csv"
# Base directories
LIMBO_DIR = os.path.expanduser("~/Desktop/limbo")
JAVA_BINDINGS_DIR = os.path.join(LIMBO_DIR, "bindings", "java")
SQLANCER_DIR = os.path.expanduser("~/Desktop/sqlancer")
TARGET_DIR = os.path.join(SQLANCER_DIR, "target")
RESULTS_BASE = os.path.join(SQLANCER_DIR, "results")
# SQLancer parameters
NUM_ITERATIONS = 100
DB_LOG_REL_PATH = os.path.join("logs", "limbo", "database0-cur.log")
TIMEOUT = 15

# YAML multiline string presenter
def str_presenter(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)
yaml.add_representer(str, str_presenter)

def run_command(cmd, cwd=None):
    """Run a command list, exit on error."""
    subprocess.run(cmd, check=True, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def setup_environment(commit_id):
    """Checkout commit and rebuild the Java bindings and SQLancer package."""
    run_command(["git", "checkout", commit_id], cwd=LIMBO_DIR)
    run_command(["make", "macos_arm64"], cwd=JAVA_BINDINGS_DIR)
    run_command(["make", "publish_local"], cwd=JAVA_BINDINGS_DIR)
    run_command(["mvn", "package", "-DskipTests"], cwd=SQLANCER_DIR)

def run_sqlancer(iteration, results_dir):
    """Run one SQLancer iteration and dump outputs to YAML in the issue folder."""
    # Clean out previous databases
    db_dir = os.path.join(TARGET_DIR, "databases")
    if os.path.exists(db_dir):
        run_command(["rm", "-rf", db_dir])

    # Prepare base command
    cmd = "java -jar sqlancer-2.0.0.jar --num-threads 1 --print-statements true --max-generated-databases 1 --num-tries 1 turso"

    # Execute SQLancer
    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            cwd=TARGET_DIR
        )
        try:
            out, err = process.communicate(timeout=TIMEOUT)
            exit_code = process.returncode
        except subprocess.TimeoutExpired:
            process.kill()
            out, err = process.communicate()
            exit_code = -1  # special code for timeout
    except Exception as e:
        out = ""
        err = f"error: {e}"
        exit_code = -2  # special code for crash

    # Read log file if present
    log_content = None
    log_path = os.path.join(TARGET_DIR, DB_LOG_REL_PATH)
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            log_content = f.read()

    # Extract seed from log and append to command string if found
    seed = None
    if log_content:
        for line in log_content.splitlines():
            if "seed value:" in line:
                seed = line.split("seed value:")[-1].strip()
                break
    if seed:
        cmd.insert(-1, seed)
        cmd.insert(-1, "--random-seed")

    # Build output dict
    output = {
        "exit_code": exit_code,
        "command": cmd,
        "stdout": out,
        "stderr": err,
        "log": log_content
    }

    # Write YAML to per-issue folder
    os.makedirs(results_dir, exist_ok=True)
    outfile = os.path.join(results_dir, f"limbo-{iteration}.yaml")
    with open(outfile, 'w') as f:
        yaml.safe_dump(output, f, indent=4, default_flow_style=False)

def main():
    # Read issues and commit IDs from CSV
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            issue = row["Issue"].strip()
            commit_ids = row["Commit IDs"].split(",")
            commit = commit_ids[0].strip()
            print(f"\n=== Processing Issue {issue} @ {commit} ===")

            # Prepare results folder for this issue
            issue_results_dir = os.path.join(RESULTS_BASE, issue)

            # 1. Checkout and build environment for this commit
            if int(issue) >= 924:
                setup_environment(commit)

                # 2. Run SQLancer iterations
                for i in range(1, NUM_ITERATIONS + 1):
                    print(f"[Issue {issue}] SQLancer iteration {i}")
                    run_sqlancer(i, issue_results_dir)

if __name__ == "__main__":
    main()

