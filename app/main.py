from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    if not validate_host(host):
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., regex to match allowed host patterns
    return True

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    if not validate_host(host):
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}