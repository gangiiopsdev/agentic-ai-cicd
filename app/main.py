from fastapi import FastAPI
import subprocess
globally_safe_hosts = {'example.com', 'localhost'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in globally_safe_hosts:
        return {"status": "denied", "reason": "Unsafe host"}
    subprocess.call(f'ping {host}', shell=True)
    return {"status": "completed"}