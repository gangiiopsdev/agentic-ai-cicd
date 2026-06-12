from fastapi import FastAPI
import subprocess
global host_whitelist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in host_whitelist:
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(f"ping {host}", shell=False)
    return {"status": "completed"}