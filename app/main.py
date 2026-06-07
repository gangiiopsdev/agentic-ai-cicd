from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of safe hosts
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Unauthorized host"}, 403