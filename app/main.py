from fastapi import FastAPI
import subprocess

global app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run instead of subprocess.call for better control and security
    if host.startswith('http') or host.startswith('https'):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
    return result.stdout

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    response = safe_ping(host)
    return {"status": "completed", "response": response}