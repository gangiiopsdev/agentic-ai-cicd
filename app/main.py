from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['safe_host1', 'safe_host2']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_safe_hosts:
        subprocess.call(f"ping {host}", shell=False)
    else:
        raise Exception("Unsafe host")
    return {"status": "completed"}