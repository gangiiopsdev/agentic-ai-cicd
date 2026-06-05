from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Safe implementation
    cmd = shlex.split(f'ping {host}')
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    cmd = shlex.split(f'ping {host}')
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}