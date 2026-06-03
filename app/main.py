from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": result.stdout}

def is_valid_host(host: str) -> bool:
    # Simple example of validation logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts