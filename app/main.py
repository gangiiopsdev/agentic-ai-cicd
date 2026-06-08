from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping", responses={200: {"description": "Ping result"}})
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host name")
    safe_host = subprocess.quote(host)
    command = ['ping', safe_host]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {"status": "completed", "host": safe_host, "output": result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}