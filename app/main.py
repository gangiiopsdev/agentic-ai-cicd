from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_secure(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}