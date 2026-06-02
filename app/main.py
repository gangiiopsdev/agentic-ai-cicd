from fastapi import FastAPI
import subprocess
cimport os
def safe_ping(host: str):
    if not host or not isinstance(host, str) or len(host) > 255:
        raise ValueError("Invalid host")
    command = ["ping", host]
    if os.name == 'nt':
        command = ['ping', '-c', host]
    subprocess.call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}