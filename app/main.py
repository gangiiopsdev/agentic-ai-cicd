from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if 'ping' in host:
        return "Invalid input"
    return subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'returncode' in result and result['returncode'] == 0:
        return {"status": "completed", "output": result['stdout']}
    else:
        return {"status": "failed", "output": result['stderr']}