from fastapi import FastAPI
import subprocess
from html import escape
cimport re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Regular expression to validate host name
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    sanitized_host = escape(host)
    subprocess.run(['ping', '-c', '1', sanitized_host], check=True)
    return {"status": "completed"}