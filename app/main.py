from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        result = subprocess.run(['ping', '-c', '1', '--', host], capture_output=True, text=True)
        return result.returncode == 0
    else:
        return False

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized host"}