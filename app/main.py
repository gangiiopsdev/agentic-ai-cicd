from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/""
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    valid_hosts = ["google.com", "example.com"]  # Example whitelist
    if host in valid_hosts:
        args = ['ping', host]
        subprocess.call(args)

    return {"status": "completed"}