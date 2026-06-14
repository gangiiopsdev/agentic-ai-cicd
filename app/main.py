from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    allowed_hosts = ['example.com', 'another.example.com']  # Replace with actual allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get("/ping")
def ping_handler(host: str):
    return ping(host)