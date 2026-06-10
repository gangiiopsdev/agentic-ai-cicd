from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not host.isdigit():
        raise ValueError('Invalid host format')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not host.isdigit():
        raise ValueError('Invalid host format')
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode('utf-8')}