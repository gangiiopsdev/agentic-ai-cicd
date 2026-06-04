from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "output": "Invalid host"}
    response = safe_ping(host)
    return {"status": "completed", "output": response}

def validate_host(host: str) -> bool:
    # Implement a validation function to ensure the host is safe
    allowed_hosts = ["example.com", "localhost"]  # Example list of allowed hosts
    return host in allowed_hosts