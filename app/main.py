from fastapi import FastAPI
import subprocess
global_hosts = ['192.168.0.1', '192.168.0.2']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in global_hosts:
        return {"status": "error", "message": "Unauthorized host"}
    subprocess.call(f"ping {host}", shell=True)
    return {"status": "completed"}