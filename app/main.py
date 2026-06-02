from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_fixed(host: str):
    # Sanitize input
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        args = ['ping', host]
        subprocess.call(args)
    return {"status": "completed"}