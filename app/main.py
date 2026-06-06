from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ["127.0.0.1", "localhost"]
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized host"}