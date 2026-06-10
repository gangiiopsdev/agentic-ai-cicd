from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with a list of arguments and shell=False
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True, shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it is safe
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid host input")
    safe_ping(host)
    return {"status": "completed"}