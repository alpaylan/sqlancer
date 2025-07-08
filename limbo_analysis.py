
import yaml
import os
import re

def is_not_implemented(result):
    stderr = result.get("stderr", "").lower()
    return ("not implemented" in stderr or
            "not supported" in stderr or
            "not yet implemented" in stderr or
            "todo" in stderr)

def is_update_c0_c0(result):
    log = result.get("log", "")
    pattern = r'UPDATE\s+(\w+)\s+SET\s*\(([^)]+)\)'
    for match in re.finditer(pattern, log):
        columns = match.group(2).split(", ")
        # two of the columns must be equal to each other
        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                if columns[i] == columns[j]:
                    return True
    return False

def is_commit_transaction(result):
    log = result.get("log", "")
    return "COMMIT TRANSACTION" in log or "COMMIT" in log or "END TRANSACTION" in log or "END" in log


if __name__ == "__main__":
    for i in range(1000):
        filename = f"results/limbo-{i}.yaml"
        try:
            with open(filename, 'r') as f:
                result = yaml.safe_load(f)
                if result is not None:
                    result["stderr"] = result.get("stderr", "").lower()

                    if is_not_implemented(result):
                        os.makedirs("results/not_implemented", exist_ok=True)
                        with open(f"results/not_implemented/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)

                    elif is_update_c0_c0(result):
                        os.makedirs("results/bug/update_c0_c0", exist_ok=True)
                        with open(f"results/bug/update_c0_c0/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_commit_transaction(result):
                        os.makedirs("results/false_positive/commit_transaction", exist_ok=True)
                        with open(f"results/false_positive/commit_transaction/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
        except FileNotFoundError:
            print(f"File {filename} not found, skipping.")
        except yaml.YAMLError as e:
            print(f"Error parsing {filename}: {e}")