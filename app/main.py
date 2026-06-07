from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ('127.0.0.1', '::1', 'localhost'):
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid or restricted host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return {"status": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}