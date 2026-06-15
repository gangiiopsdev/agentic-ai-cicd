from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

# Function to validate the host input
def validate_host(host):
    # Add validation logic here
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}