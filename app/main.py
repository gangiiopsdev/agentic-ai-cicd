from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    # Secure implementation using subprocess.run with shell=False and safe arguments
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}