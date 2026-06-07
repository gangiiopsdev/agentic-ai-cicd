from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not safe_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}