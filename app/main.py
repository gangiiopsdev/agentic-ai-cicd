from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run
    if not is_valid_host(host):
        return {"status": "error", "output": "Invalid host"}
    result = subprocess.run(['ping', '-c', '1', re.escape(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

def is_valid_host(host: str) -> bool:
    # Add validation logic for the host input
    allowed_hosts = [re.escape(host) for host in ['example.com', 'localhost']]
    return re.fullmatch('|'.join(allowed_hosts), host)