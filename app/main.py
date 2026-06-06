from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host name")
    safe_host = subprocess.quote(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host name")
    safe_host = subprocess.quote(host)
    return {"status": "completed", "host": safe_host}