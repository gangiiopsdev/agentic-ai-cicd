from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it is a safe value
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Safe implementation using subprocess.run with shell=False and explicit arguments
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Implement input validation logic here
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts