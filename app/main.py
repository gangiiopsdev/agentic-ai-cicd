from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host != 'localhost' and not host.startswith('127.0.0.1'):
        return {"status": "failed", "error": "Invalid host"}
    # Sanitize input by replacing potentially dangerous characters
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
    try:
        result = subprocess.run(['ping', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}