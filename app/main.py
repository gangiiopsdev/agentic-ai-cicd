from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run with proper validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with proper validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}