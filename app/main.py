from fastapi import FastAPI
import subprocess
import shlex
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
def ping(host: str):
    try:
        command = f'ping -c 4 {shlex.quote(host)}'
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}