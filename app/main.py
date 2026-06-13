from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if 'ping' in host:
        return "Invalid host name"
    return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}