from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper argument handling
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host'}
    return ping(host)