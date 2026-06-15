from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True, shell=False)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }