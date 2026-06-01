from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run to avoid shell=True and partial paths
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to prevent injection attacks
    if not all(c.isalnum() or c in '.-\' for c in host):
        raise ValueError('Invalid host name')
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}