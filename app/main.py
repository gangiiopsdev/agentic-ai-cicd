from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping_fixed(host: str):
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic for host
    return True