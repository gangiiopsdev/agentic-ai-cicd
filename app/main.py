from fastapi import FastAPI
import subprocess
import shlex
cimport = subprocess.CalledProcessError

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}

    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}