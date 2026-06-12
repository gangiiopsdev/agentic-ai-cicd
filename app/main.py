from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def ping(host: str):
    if not cmd_re.match(host):
        return {"status": "failed", "error": "Invalid hostname"}

    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}