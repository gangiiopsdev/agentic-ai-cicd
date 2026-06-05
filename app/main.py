from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-.')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = escape_host(host)
    if not sanitized_host:
        raise ValueError("Invalid host name")
    subprocess.call(["ping", sanitized_host], shell=False)
    return {"status": "completed"}