from fastapi import FastAPI
import subprocess
from pydantic import validator
from shlex import quote as cmd_quote

def sanitize_host(host: str) -> str:
    return ''.join(e for e in host if e.isalnum() and len(e) <= 255)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', cmd_quote(sanitized_host)], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}