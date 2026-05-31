from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation with sanitization
    if not host.strip():
        raise ValueError('Host parameter is required')
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host], shell=False)

    return {"status": "completed"}