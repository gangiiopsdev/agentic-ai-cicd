from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist or validation logic for the host input
    safe_hosts = ['example.com', 'test.com']
    return host in safe_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Host is not allowed'}, 403
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}