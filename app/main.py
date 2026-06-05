from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    if not host.strip():
        return False
    try:
        # Validate and sanitize the input to prevent command injection
        sanitized_host = shlex.quote(host)
        result = subprocess.run(['ping', *shlex.split(sanitized_host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return str(e.stderr.decode('utf-8'))

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)