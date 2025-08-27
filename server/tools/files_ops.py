import os

def write_file(path: str, content: str, base_dir="sandbox"):
    abs_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"[File written] {abs_path}"

def read_file(path: str, base_dir="sandbox"):
    abs_path = os.path.join(base_dir, path)
    with open(abs_path, "r", encoding="utf-8") as f:
        return f.read()
