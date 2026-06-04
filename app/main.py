from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host name")
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}