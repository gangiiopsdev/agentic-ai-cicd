from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host")
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}