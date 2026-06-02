from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Host not allowed'}
    # Fixed implementation using subprocess.run with shell=False and a list of arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}