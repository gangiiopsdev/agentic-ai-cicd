from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()  # Remove any leading/trailing whitespace
    if valid_hostname(safe_host):
        subprocess.call(['ping', safe_host])
    return {"status": "completed"}

# Function to validate hostname
def valid_hostname(hostname: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{,61}[a-zA-Z0-9])?$'
    return re.match(pattern, hostname) is not None