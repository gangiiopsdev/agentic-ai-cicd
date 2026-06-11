from fastapi import FastAPI
import subprocess
import re

def generate_ping_command(host: str) -> list:
    if not validate_host(host):
        raise ValueError("Invalid host")
    return ['ping', host]

def validate_host(host: str) -> bool:
    # Implement a simple validation logic for the host
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        return False
    return '.' in host

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(generate_ping_command(host), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}