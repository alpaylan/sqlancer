
import yaml
import os
import re

def is_not_implemented(result):
    stderr = result.get("stderr", "").lower()
    return ("not implemented" in stderr or
            "not supported" in stderr or
            "not yet implemented" in stderr or
            "todo" in stderr or
            "no such module" in stderr or
            "not a valid pragma name" in stderr or
            "no such table: sqlite_stat1" in stderr or
            "only passive mode supported" in stderr or
            "create index is disabled by default" in stderr)

def is_update_c0_c0(result):
    checked = result.get("log", "")
    if checked is None: checked = result.get("stderr", "")
    pattern = r'update\s+(\w+)\s+\w*\s*\w*\s*set\s*\(([^)]+)\)'
    for match in re.finditer(pattern, checked):
        columns = match.group(2).split(", ")
        # two of the columns must be equal to each other
        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):
                if columns[i] == columns[j]:
                    return True
    return False

def is_commit_transaction(result):
    log = result.get("log", "")
    if log is None: return False
    return "COMMIT TRANSACTION" in log or "COMMIT" in log or "END TRANSACTION" in log or "END" in log

def is_invalid_step(result):
    stderr = result.get("stderr", "").lower()
    return "step() returned invalid result" in stderr

def is_like_on_nontext(result):
    stderr = result.get("stderr", "").lower()
    return "internal error: entered unreachable code: like on non-text registers" in stderr

def is_invalid_page_type(result):
    stderr = result.get("stderr", "").lower()
    return "called `result::unwrap()` on an `err` value: corrupt(\"invalid page type: 1\")" in stderr

def is_optimize_no_rewrite(result):
    stderr = result.get("stderr", "").lower()
    return "internal error: entered unreachable code: expression should have been rewritten" in stderr

def is_id_rewrite_as_col(result):
    stderr = result.get("stderr", "").lower()
    return "id should have been rewritten as column" in stderr

def is_header_sz_gt_nr(result):
    stderr = result.get('stderr', "").lower()
    return "assertion failed: (header_size as usize) >= nr" in stderr

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
                    elif is_commit_transaction(result):
                        os.makedirs("results/false_positive/commit_transaction", exist_ok=True)
                        with open(f"results/false_positive/commit_transaction/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_like_on_nontext(result):
                        os.makedirs("results/bug/like_on_nontext", exist_ok=True)
                        with open(f"results/bug/like_on_nontext/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_invalid_page_type(result):
                        os.makedirs("results/bug/invalid_page_type", exist_ok=True)
                        with open(f"results/bug/invalid_page_type/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_optimize_no_rewrite(result):
                        os.makedirs("results/bug/optimizer_should_rewrite", exist_ok=True)
                        with open(f"results/bug/optimizer_should_rewrite/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_id_rewrite_as_col(result):
                        os.makedirs("results/bug/id_should_rewrite_as_col", exist_ok=True)
                        with open(f"results/bug/id_should_rewrite_as_col/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_header_sz_gt_nr(result):
                        os.makedirs("results/bug/header_sz_gt_nr", exist_ok=True)
                        with open(f"results/bug/header_sz_gt_nr/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_update_c0_c0(result):
                        os.makedirs("results/bug/update_c0_c0", exist_ok=True)
                        with open(f"results/bug/update_c0_c0/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
                    elif is_invalid_step(result):
                        os.makedirs("results/bug/invalid_step", exist_ok=True)
                        with open(f"results/bug/invalid_step/limbo-{i}.yaml", 'w') as f:
                            yaml.safe_dump(result, f, indent=4, default_flow_style=False, allow_unicode=True)
                        os.remove(filename)
        except FileNotFoundError:
            #print(f"File {filename} not found, skipping.")
            pass
        except yaml.YAMLError as e:
            print(f"Error parsing {filename}: {e}")
