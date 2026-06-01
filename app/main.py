from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Whitelist of allowed hosts
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        sanitized_host = subprocess.quote(host)
        subprocess.call(["ping", sanitized_host])
        return {"status": "completed"}
    else:
        return {"status": "host not allowed"}