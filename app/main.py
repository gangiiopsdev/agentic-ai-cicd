from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    allowed_hosts = ["example.com", "127.0.0.1"]
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        return {"status": "denied"}
    return {"status": "completed"}