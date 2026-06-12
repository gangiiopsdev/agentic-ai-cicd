from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host(host)
    subprocess.call(["ping", host])
    return {"status": "completed"}