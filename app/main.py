from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return "Invalid host"
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not is_valid_host(host):
        return "Invalid host"
    subprocess.call(['ping', host])

def is_valid_host(host: str) -> bool:
    # Simple validation to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    for char in host:
        if char not in allowed_chars:
            return False
    return True