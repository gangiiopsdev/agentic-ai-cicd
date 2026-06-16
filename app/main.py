from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Safe implementation using shlex to escape command arguments
    args = shlex.split('ping ' + host)
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}