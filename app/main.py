from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host])

@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host
    return True