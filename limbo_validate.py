import subprocess
import sys
import yaml

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python limbo_validate.py <path_to_yaml_file>")
    sys.exit(1)

# Load the YAML file
yaml_file_path = sys.argv[1]
try:
    with open(yaml_file_path, 'r') as file:
        result = yaml.safe_load(file)
except FileNotFoundError:
    print(f"File {yaml_file_path} not found.")
    sys.exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")
    sys.exit(1)

# Validate the contents of the YAML file
if not isinstance(result, dict):
    print("Invalid YAML format: Expected a mapping (dictionary) at the root.")
    sys.exit(1)

# Check for required keys in the YAML
required_keys = ['stderr', 'stdout', 'log', 'command']
for key in required_keys:
    if key not in result:
        print(f"Missing required key in YAML: {key}")
        sys.exit(1)

sql_statements = result.get('log', '').split(';')

limbo_path = "/Users/akeles/Programming/projects/limbo/target/debug/tursodb"

# Create an interactive shell session
process = subprocess.Popen(
    [limbo_path],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1,
    universal_newlines=True
)
# Check if the process started successfully
if process is None:
    print("Failed to start the process.")
    sys.exit(1)

for statement in sql_statements:
    statement = statement.strip()
    if not statement:
        continue  # Skip empty statements
    # Send the SQL command to the process
    process.stdin.write(statement + ";" + '\n')
    print(f"{statement};")
    process.stdin.flush()

# Read the output and error streams
stdout, stderr = process.communicate(timeout=5)  # Set a timeout for the command execution
# Print the output and error streams
print("STDOUT:", stdout)
print("STDERR:", stderr)
# Close the process
process.stdin.close()
process.stdout.close()
process.stderr.close()
process.wait()
# Clean up the process
process.terminate()
process.wait()
print("Process terminated")
