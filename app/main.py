from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts

@app.get("/ping")
def ping(host: str):
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Host is not allowed"}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}