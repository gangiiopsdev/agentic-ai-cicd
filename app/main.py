from fastapi import FastAPI
import subprocess
from pydantic import validator
from shlex import quote as cmd_quote

def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum() and len(e) <= 255)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.net']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    sanitized_host = cmd_quote(sanitized_host)
    result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}