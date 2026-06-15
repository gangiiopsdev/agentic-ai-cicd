from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and escaping
    allowed_ips = ['127.0.0.1', '::1']  # Example allowed IPs
    if host in allowed_ips:
        args = ['ping', '--shell-escape', host]
        subprocess.call(args, shell=True)
    return {"status": "completed"}