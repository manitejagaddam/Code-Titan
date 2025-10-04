
class CriticAgent:
    def review(self, files: list):
        for f in files:
            if not f["content"]:
                raise ValueError(f"{f['filename']} is empty!")
        print("✅ All files passed basic validation.")
