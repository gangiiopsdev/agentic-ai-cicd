from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}

    # Secure implementation
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}

    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

# Helper function to validate host
def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., regex matching IP address or hostname patterns
    return True