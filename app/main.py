from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if re.match(r'^[a-zA-Z0-9-.!@#$%^&*()]*$', e))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9-.!@#$%^&*()]*$', sanitized_host):
        return {"error": "Invalid host"}, 400
    subprocess.run(shlex.split(f'ping {sanitized_host}'))
    return {"status": "completed"}