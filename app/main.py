from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isalnum():
        return subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}