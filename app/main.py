from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with full path and validation
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {'status': 'error', 'message': 'Invalid host'}

    if host in ['8.8.8.8', '127.0.0.1']:  # Add more valid hosts as needed
        result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Invalid host'}