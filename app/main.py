from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    if host not in ['127.0.0.1', '::1']:  # Add more allowed hosts as needed
        return
    args = shlex.split(f'ping {host}')
    subprocess.run(args)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}