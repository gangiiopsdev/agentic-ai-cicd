from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts

def is_safe_host(host):
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    # Secure implementation using subprocess.run with shell=False and args parameter
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}