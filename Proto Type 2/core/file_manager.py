import os


class FileManager:
    
    def write_file(self, file_name : str, content : str, output_dir = "output") -> None:
        os.makedirs(output_dir, exist_ok=True)
        path = os.path.join(output_dir, file_name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"💾 Saved: {file_name} in {path}")
        