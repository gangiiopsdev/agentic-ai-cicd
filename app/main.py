from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = {'example.com', 'another-example.com'}

@app.get('/ping')
def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    # Fixed implementation using subprocess.run with shell=False and a list of arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}