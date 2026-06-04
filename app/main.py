from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

def validate_host(host):
    # Simple validation to check if the host is a valid IP address or hostname
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        sanitized_host = sanitize_input(host)
        subprocess.call(['ping', sanitized_host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400