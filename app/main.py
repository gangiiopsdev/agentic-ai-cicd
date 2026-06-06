from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run instead of subprocess.call for better security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'response': 'Invalid host'}
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}

def is_valid_host(host):
    # Implement validation logic to ensure the host input is safe
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts