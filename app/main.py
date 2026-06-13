from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Simple validation logic, replace with more robust checks
    return '.' in host and len(host.split('.')) == 4

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)