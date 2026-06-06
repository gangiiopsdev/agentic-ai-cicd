from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid hostname")
    return subprocess.call(['ping', host])

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