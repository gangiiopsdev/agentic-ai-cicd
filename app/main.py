from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or not os.path.exists(host):
        return {"error": "Invalid host"}
    # Use a safe way to execute commands with user-provided input
    subprocess.run(["ping", "/bin/sh", "-c", f'ping -c 1 {host}'], check=True)
    return {"status": "completed"}