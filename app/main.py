from fastapi import FastAPI
import subprocess
def sanitize_hostname(hostname):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-'
    return ''.join(c for c in hostname if c in allowed_chars)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_hostname(host)
    if not sanitized_host:
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}