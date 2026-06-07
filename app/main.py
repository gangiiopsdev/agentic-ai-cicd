from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Simple validation example, replace with more robust checks as needed
    return all(c.isalnum() or c in ['.', '-'] for c in host)