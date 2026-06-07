from fastapi import FastAPI
import subprocess
global allowed_hosts = ['127.0.0.1', '::1']

def validate_host(host):
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise HTTPException(status_code=403, detail="Host not allowed")
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}