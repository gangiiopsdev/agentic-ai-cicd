from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Add your validation logic here
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)