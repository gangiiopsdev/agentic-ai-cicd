from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command: str, args: list):
    full_command = [command] + shlex.split(' '.join(args))
    subprocess.run(full_command, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:  # Restrict allowed hosts
        return {"status": "failed", "message": "Invalid host"}
    safe_subprocess("/bin/ping", [host])
    return {"status": "completed"}