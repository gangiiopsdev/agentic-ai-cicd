from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    # Safe implementation using subprocess.run with proper argument passing
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}