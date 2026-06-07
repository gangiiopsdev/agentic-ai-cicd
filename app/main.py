from fastapi import FastAPI
import subprocess
def is_safe_host(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']  # Example allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', f'--{host}'], check=True, capture_output=True)
    return {"status": "completed"}