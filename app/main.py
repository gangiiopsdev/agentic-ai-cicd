from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    args = shlex.split(f'ping -c 4 {host}')  # Limit the number of pings to prevent DoS
    result = subprocess.run(args, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "errors": result.stderr
    }