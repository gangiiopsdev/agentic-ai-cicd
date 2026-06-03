from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use a whitelist of allowed hosts or validate input
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    subprocess.call(['ping', host], shell=False)  # Added shell=False to prevent shell injection
    return {'status': 'completed'}