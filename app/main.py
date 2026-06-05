from fastapi import FastAPI
import subprocess
global ping_hosts
ping_hosts = {"google.com": True, "example.com": True}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in ping_hosts:
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}