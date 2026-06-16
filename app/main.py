from fastapi import FastAPI
import subprocess
def safe_subprocess(command):
    return subprocess.run(command, check=True, capture_output=True)
git.from_subprocess = safe_subprocess