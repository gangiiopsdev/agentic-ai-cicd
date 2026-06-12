from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if '.' not in host and ':' not in host:
        return 'Invalid host'
    return subprocess.call(['ping', '-c', '1', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result == 0:
        return {"status": "completed", "result": "Success"}
    else:
        return {"status": "failed", "result": "Failed"}