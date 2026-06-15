from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only alphanumeric characters and a few special characters
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return all(char in allowed_chars for char in host)