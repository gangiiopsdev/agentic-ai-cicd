from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a list of safe hosts or use regex to validate the host input
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        # Secure implementation
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid or unsafe host')

    return {"status": "completed"}