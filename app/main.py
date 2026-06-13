from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    return host.isalnum() and '.' in host

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "output": "Invalid host"}
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}