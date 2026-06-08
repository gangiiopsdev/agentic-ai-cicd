from fastapi import FastAPI
import subprocess
import shlex

def sanitize_input(input_string):
    return ''.join(ch if ch.isalnum() or ch in ['.', '-', '_'] else '_' for ch in input_string)

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Example list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}

    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}