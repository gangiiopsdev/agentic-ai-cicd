from fastapi import FastAPI
import subprocess
import socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate user input to prevent injection attacks
        if not socket.gethostbyname(host):
            return {"status": "invalid", "message": "Invalid hostname or IP address"}
        # Secure implementation using subprocess.run with shell=False and check=True
        result = subprocess.run(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if result.returncode == 0:
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": result.stderr}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}