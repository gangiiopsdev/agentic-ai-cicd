from fastapi import FastAPI
import subprocess
from shlex import quote
generate_ping_command = lambda host: ['ping', quote(host)]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.call(generate_ping_command(host))
    return {"status": "completed"}

# Function to validate and sanitize the host input
def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., checking for allowed domains or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts