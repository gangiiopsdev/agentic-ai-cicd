from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid host"
    return subprocess.call(['ping', host], capture_output=True, text=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int) and result == 0:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": result}