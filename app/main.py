from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', '-c 1', host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts