from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}

# Helper function to validate the host
def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    try:
        result = subprocess.run(['nslookup', host], check=True, text=True)
        return any(host in line for line in result.stdout.splitlines())
    except subprocess.CalledProcessError:
        return False