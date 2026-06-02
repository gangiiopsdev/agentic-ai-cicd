from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

# Helper function to validate host input
def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts