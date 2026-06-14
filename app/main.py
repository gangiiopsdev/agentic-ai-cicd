from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-'])

def validate_host(host: str):
    allowed_hosts = {'example.com', 'test.com'}  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    validate_host(sanitized_host)
    # Secure implementation
    subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, capture_output=True)
    return {"status": "completed"}