from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_. '
    sanitized = ''.join(char for char in input if char in allowed_chars)
    return sanitized

def is_safe_host(host):
    safe_hosts = ['example.com', 'test.com']  # List of allowed hosts
    return host in safe_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        host = sanitize_input(host)
        # Safe implementation with shell=False and full path
        subprocess.call(["/usr/bin/ping", host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400