from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and safe arguments
    if not host.startswith(".") and validate_host(host):
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}

def validate_host(host: str) -> bool:
    # Simple validation to check if the host contains only allowed characters
    return all(c.isalnum() or c in '-.' for c in host)