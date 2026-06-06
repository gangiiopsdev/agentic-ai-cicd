from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c == '.')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"status": "error", "message": "Invalid host parameter"}
    subprocess.run(['ping', sanitized_host], check=True, shell=False)
    return {"status": "completed"}