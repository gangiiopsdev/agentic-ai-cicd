from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

# Define a whitelist of allowed hostnames/IP addresses
ALLOWED_HOSTS = ['127.0.0.1', '::1']

def validate_input(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid input")
    return host in ALLOWED_HOSTS

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    if validate_input(host):
        try:
            result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Invalid input"}