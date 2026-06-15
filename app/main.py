from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    valid_hosts = ['localhost', '127.0.0.1']
    if host not in valid_hosts:
        raise ValueError("Invalid host")
    # Using f-string for safe command execution
    cmd = f'ping {host}'
    subprocess.run(cmd, shell=False, check=True)
app = FastAPI()
@app.get="/home"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}