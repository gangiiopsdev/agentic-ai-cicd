from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Define a whitelist of allowed hosts
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        subprocess.run(["ping", host], check=True, capture_output=True)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)