from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and proper validation of host input
    if not is_valid_host(host):
        return {'status': 'invalid_host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Add validation logic here to ensure the host input is safe
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping_endpoint(host: str):    return ping(host)