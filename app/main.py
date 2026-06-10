from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Validate the host input to ensure it's a safe target for pinging
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

# Function to validate the host input
def is_safe_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only certain IP addresses or domain names
    allowed_hosts = ['example.com', '127.0.0.1']  # Example list
    return host in allowed_hosts