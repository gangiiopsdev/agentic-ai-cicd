from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation without using shell=True
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent shell injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check for allowed characters or IP address format
    return all(c.isalnum() or c in ('.', '-') for c in host)