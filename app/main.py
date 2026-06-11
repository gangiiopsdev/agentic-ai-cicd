from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if sanitize_host(host):  # Sanitize the host input
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}