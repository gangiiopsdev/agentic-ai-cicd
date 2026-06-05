from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.startswith(('127.', '::ffff:127.', 'localhost', '0.0.0.0')):
        return False
    return True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(["ping", host])
    return {"status": "completed"}