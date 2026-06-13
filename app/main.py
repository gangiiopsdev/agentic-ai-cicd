from fastapi import FastAPI
import subprocess
from shlex import quote
import os
import re

def safe_ping(host: str):
    try:
        result = subprocess.run(["ping", "-c", "1", quote(host)], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host: str) -> bool:
    ip_pattern = re.compile(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$')
    hostname_pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(ip_pattern.match(host)) or bool(hostname_pattern.match(host))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return "Invalid host"
    return safe_ping(host)