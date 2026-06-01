from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": "error"}