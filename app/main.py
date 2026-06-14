from fastapi import FastAPI
import subprocess
from os.path import abspath, expandvars

app = FastAPI()

def safe_ping(host):
    try:
        cmd = ['ping', host]
        if not all(cmd_part.isalnum() or cmd_part in '-.' for cmd_part in cmd[1:]):
            raise ValueError('Invalid hostname')
        expanded_cmd = [expandvars(abspath(cmd_part)) for cmd_part in cmd]
        subprocess.run(expanded_cmd, check=True, timeout=5)
        return True
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f'Ping failed: {e}')
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed", "result": True}
    else:
        return {"status": "failed", "result": False}