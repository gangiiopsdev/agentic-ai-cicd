from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Safe implementation using subprocess.run and avoiding shell=True
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        raise ValueError(f'Ping failed: {e}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure the host input is sanitized or validated
    if not validate_host(host):
        raise ValueError('Invalid host')
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}
def validate_host(host: str) -> bool:
    # Implement validation logic here
    return host.isalnum() and len(host) > 0