from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.replace('.', '').isdigit() and len(host) <= 15

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}