from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Define allowed hosts
    if host not in allowed_hosts:
        return False
    return True

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise Exception("Invalid host")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}