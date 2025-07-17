#!/usr/bin/env python3

import csv
import subprocess
import os
import sys

"""
Potential pitfalls;

1. pom.xml

Early:
    <groupId>org.github.tursodatabase</groupId>
    <artifactId>limbo</artifactId>
    <version>0.0.1-SNAPSHOT</version>

Late:
    <groupId>tech.turso</groupId>
    <artifactId>turso</artifactId>
    <version>0.0.1-SNAPSHOT</version>

2. runner

Limbo:
    java -jar sqlancer-2.0.0.jar --num-threads 1 --print-statements true --max-generated-databases 1 --num-tries 1 limbo

SQLiteLimbo:
    java -jar sqlancer-2.0.0.jar --num-threads 1 --print-statements true --max-generated-databases 1 --num-tries 1 turso

3. connection string

In old ones:
    jdbc:sqlite:

In new ones:
    jdbc:turso:

4. getString in LimboSchema.java

In old ones:
    rs.getString(1);

In new ones:
    rs.getString("name");
"""

# --- Configuration ---
# Path to the CSV file
CSV_FILE = "issues.csv"
# Base directories
LIMBO_DIR = os.path.expanduser("~/Programming/projects/limbo")
JAVA_BINDINGS_DIR = os.path.join(LIMBO_DIR, "bindings", "java")
SQLANCER_DIR = os.path.expanduser("~/Programming/projects/sqlancer")
TARGET_DIR = os.path.join(SQLANCER_DIR, "target")
RESULTS_BASE = os.path.join(SQLANCER_DIR, "results")
# SQLancer parameters
NUM_ITERATIONS = 100
DB_LOG_REL_PATH = os.path.join("logs", "limbo", "database0-cur.log")
TIMEOUT = 15

def fix_pom_xml():
    old_limbo = {
        "groupId": "org.github.tursodatabase",
        "artifactId": "limbo",
        "version": "0.0.1-SNAPSHOT"
    }
    mid_limbo = {
        "groupId": "tech.turso",
        "artifactId": "limbo",
        "version": "0.0.1-SNAPSHOT"
    }
    new_limbo = {
        "groupId": "tech.turso",
        "artifactId": "turso",
        "version": "0.0.1-SNAPSHOT"
    }

    gradle_file = os.path.join(LIMBO_DIR, "bindings", "java", "build.gradle.kts")

    with open(gradle_file, "r") as file:
        content = file.read()
        if "groupId = \"tech.turso\"" in content and "artifactId = \"turso\"" in content:
            version = new_limbo
        elif "groupId = \"tech.turso\"" in content and "artifactId = \"limbo\"" in content:
            version = mid_limbo
        elif "group = \"org.github.tursodatabase\"" in content:
            version = old_limbo
        else:
            print(content)
            exit("Unknown version in gradle file, cannot fix pom.xml")
     
    pom_file = os.path.join(SQLANCER_DIR, "pom.xml")
    with open(pom_file, "r") as file:
        # find the <!-- limbo --> comment
        content = file.read()
        start_index = content.find("<!-- limbo -->")
        if start_index == -1:
            exit("Could not find <!-- limbo --> comment in pom.xml")
        end_index = content.find("</dependency>", start_index) + len("</dependency>")
        if end_index == -1:
            exit("Could not find </dependency> tag in pom.xml")
        # Replace the content between the comments with the new version
        new_content = f"""<!-- limbo -->
            <groupId>{version['groupId']}</groupId>
            <artifactId>{version['artifactId']}</artifactId>
            <version>{version['version']}</version>
        </dependency>"""
        content = content[:start_index] + new_content + content[end_index:]

    with open(pom_file, "w") as file:
        file.write(content)
        file.write("\n")
        print(f"Updated pom.xml with {version['groupId']}:{version['artifactId']}:{version['version']}")

def fix_connection_string():
    old_string = "jdbc:sqlite:"
    new_string = "jdbc:turso:"
    search_dir = os.path.join(LIMBO_DIR, "bindings", "java", "src", "main", "java")
    # check for String VALID_URL_PREFIX = "jdbc:sqlite:" or String VALID_URL_PREFIX = "jdbc:turso:"
    conn_string = None
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    if old_string in content:
                        conn_string = old_string
                    elif new_string in content:
                        conn_string = new_string

    if conn_string is None:
        exit("Could not find connection string in Java files")

    # Replace the connection string in SQLancer
    path = os.path.join(SQLANCER_DIR, "src", "sqlancer", "limbo", "LimboProvider.java")
    with open(path, "r") as file:
        content = file.read()
        if old_string in content and conn_string != old_string:
            content = content.replace(old_string, conn_string)
            print(f"Updated connection string in {path} from {old_string} to {new_string}")
        elif new_string in content and conn_string != new_string:
            content = content.replace(new_string, conn_string)
            print(f"Updated connection string in {path} from {new_string} to {old_string}")
        else:
            print(f"No changes needed for connection string in {path}")
    with open(path, "w") as file:
        file.write(content)
        
    path = os.path.join(SQLANCER_DIR, "src", "sqlancer", "limbosqlite3", "LimboSQLite3Provider.java")
    with open(path, "r") as file:
        content = file.read()
        if old_string in content and conn_string != old_string:
            content = content.replace(old_string, conn_string)
            print(f"Updated connection string in {path} from {old_string} to {new_string}")
        elif new_string in content and conn_string != new_string:
            content = content.replace(new_string, conn_string)
            print(f"Updated connection string in {path} from {new_string} to {old_string}")
        else:
            print(f"No changes needed for connection string in {path}")
    with open(path, "w") as file:
        file.write(content)

    print("Updated connection strings in {path}")


def run_command(cmd, cwd=None):
    """Run a command list, exit on error."""
    print(f"Running command: {' '.join(cmd)} in {cwd or os.getcwd()}")
    subprocess.run(cmd, check=True, cwd=cwd, stdout=sys.stdout, stderr=sys.stderr)


def setup_environment(commit_id):
    """Checkout commit and rebuild the Java bindings and SQLancer package."""
    run_command(["git", "checkout", commit_id], cwd=LIMBO_DIR)
    run_command(["cargo", "clean"], cwd=LIMBO_DIR)
    run_command(["make", "macos_arm64"], cwd=JAVA_BINDINGS_DIR)
    run_command(["make", "publish_local"], cwd=JAVA_BINDINGS_DIR)
    fix_pom_xml()
    fix_connection_string()
    run_command(["mvn", "package", "-DskipTests"], cwd=SQLANCER_DIR)

def cleanup_environment():
    run_command(["rm", "-rf", "target"], cwd=SQLANCER_DIR)
    run_command(["rm", "-rf", "~/.m2/repository/org/github/tursodatabase/limbo"], cwd=None)
    run_command(["rm", "-rf", "~/.m2/repository/tech/turso/limbo"], cwd=None)
    run_command(["rm", "-rf", "~/.m2/repository/tech/turso/turso"], cwd=None)

def run_sqlancer(iteration, results_dir):
    """Run one SQLancer iteration and dump outputs to YAML in the issue folder."""
    # Clean out previous databases
    out_dir = os.path.join(results_dir, f"iter-{iteration}")
    if os.path.exists(out_dir):
        out_files = ["exit_code.txt", "command.txt", "stdout.txt", "stderr.txt"]
        if all(os.path.exists(os.path.join(out_dir, f)) for f in out_files):
            # Skip if all expected output files already exist
            print(f"Output directory {out_dir} already exists, skipping iteration {iteration}.")
            return

    db_dir = os.path.join(TARGET_DIR, "databases")
    if os.path.exists(db_dir):
        run_command(["rm", "-rf", db_dir])

    # Prepare base command
    cmd = [
        "java",
        "-jar",
        "sqlancer-2.0.0.jar",
        "--num-threads",
        "1",
        "--print-statements",
        "true",
        "--max-generated-databases",
        "1",
        "--num-tries",
        "1",
        "turso",
    ]

    # Execute SQLancer
    try:
        process = subprocess.Popen(
            " ".join(cmd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            cwd=TARGET_DIR,
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
        with open(log_path, "r") as f:
            log_content = f.read()

    # Extract seed from log and append to command string if found
    seed = None
    if log_content:
        for line in log_content.splitlines():
            if "seed value:" in line:
                seed = line.split("seed value:")[-1].strip()
                break
    if seed:
        cmd.insert(-1, "--random-seed")
        cmd.insert(-1, seed)

    # Build output dict
    output = {
        "exit_code": exit_code,
        "command": " ".join(cmd),
        "stdout": out,
        "stderr": err,
        "log": log_content,
    }

    # Write YAML to per-issue folder
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "exit_code.txt"), "w") as outfile:
        outfile.write(str(exit_code))
    with open(os.path.join(out_dir, "command.txt"), "w") as outfile:
        outfile.write(output["command"])
    with open(os.path.join(out_dir, "stdout.txt"), "w") as outfile:
        outfile.write(output["stdout"])
    with open(os.path.join(out_dir, "stderr.txt"), "w") as outfile:
        outfile.write(output["stderr"])
    if output["log"]:
        with open(os.path.join(out_dir, "log.txt"), "w") as outfile:
            outfile.write(output["log"])


def is_complete(issue):
    """Check if the issue has already been processed."""
    issue_dir = os.path.join(RESULTS_BASE, issue)
    if not os.path.exists(issue_dir):
        return False
    # Check if all 100 iterations have output files
    for i in range(1, NUM_ITERATIONS + 1):
        iter_dir = os.path.join(issue_dir, f"iter-{i}")
        if not os.path.exists(iter_dir):
            return False
        out_files = ["exit_code.txt", "command.txt", "stdout.txt", "stderr.txt"]
        if not all(os.path.exists(os.path.join(iter_dir, f)) for f in out_files):
            return False
    return True

def main():
    # Read issues and commit IDs from CSV
    with open(CSV_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            issue = row["Issue"].strip()
            commit_ids = row["Commit IDs"].split(",")
            commit = commit_ids[0].strip()
            print(f"\n=== Processing Issue {issue} @ {commit} ===")

            # Prepare results folder for this issue
            issue_results_dir = os.path.join(RESULTS_BASE, issue)

            # 1. Checkout and build environment for this commit
            if int(issue) >= 924 and not is_complete(issue):
                setup_environment(commit)

                # 2. Run SQLancer iterations
                for i in range(1, NUM_ITERATIONS + 1):
                    print(f"[Issue {issue}] SQLancer iteration {i}")
                    run_sqlancer(i, issue_results_dir)

                cleanup_environment()

if __name__ == "__main__":
    cleanup_environment()
    main()
