from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if not host or ' ' in host:
        return "Invalid host"
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": "completed", "output": status}