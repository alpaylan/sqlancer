
# run rm -rf databases && java -jar sqlancer-2.0.0.jar --num-threads 1 --print-statements true --max-generated-databases 1 --num-tries 10 limbo in target/

import subprocess
import os
import json
import yaml

def str_presenter(dumper, data):
    if "\n" in data:  # Only apply for multiline strings
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)

def run_sqlancer():
    # Define the command to run SQLancer
    # Go to target directory
    os.chdir("target")

    # Remove the databases directory if it exists
    if os.path.exists("databases"):
        subprocess.run(["rm", "-rf", "databases"])

    command = [
        "java", "-jar", "sqlancer-2.0.0.jar",
        "--num-threads", "1",
        "--print-statements", "true",
        "--max-generated-databases", "1",
        "--num-tries", "1",
        "limbo"
    ]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Read 
    # Print the output
    
    out = result.stdout
    err = result.stderr
    log = None

    # read the `logs/limbo/database0-cur.log` file
    log_file_path = "logs/limbo/database0-cur.log"
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            log = str(log_file.read())


    # Extract seed value from the log
    seed = None
    if log is not None:        
        for line in log.splitlines():
            if "seed value:" in line:
                seed = line.split("seed value: ")[1].strip()
                break

    # move up one directory
    os.chdir("..")
    # Add a new JSON file with the output

    if seed is not None:
        command.insert(len(command) - 2, f"--random-seed {seed}")
    
    # count the number of results
    os.makedirs("results", exist_ok=True)
    num_results = len(os.listdir("results"))

    output = {
        "stdout": out,
        "stderr": err,
        "log": log,
        "command": " ".join(command)
    }

    filename = f"results/limbo-{num_results}.yaml"

    with open(filename, 'w') as f:
        yaml.safe_dump(output, f, indent=4, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    for i in range(1000):
        print(f"Running SQLancer iteration {i + 1}...")
        run_sqlancer()