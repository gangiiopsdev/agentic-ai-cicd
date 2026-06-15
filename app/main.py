from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list of args instead of shell=True
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    safe_ping(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed characters or patterns
    return all(c.isalnum() or c in ['.', '-'] for c in host)