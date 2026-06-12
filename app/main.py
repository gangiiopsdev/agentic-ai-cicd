from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

def is_safe_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of safe hosts
    return host in allowed_hosts