import subprocess
import os

def run_command(cmd: str, work_dir="sandbox"):
    """
    Run a shell command inside the sandbox.
    Returns: dict with stdout, stderr, exit_code
    """
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=work_dir,
            capture_output=True,
            text=True,
            timeout=60
        )
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "exit_code": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": "Command timed out", "exit_code": -1}
