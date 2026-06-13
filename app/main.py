from fastapi import FastAPI
import subprocess
global allowlist_hosts = ['127.0.0.1', 'localhost']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in allowlist_hosts:
        raise HTTPException(status_code=400, detail="Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}