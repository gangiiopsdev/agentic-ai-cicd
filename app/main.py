from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious content
    if any(char in host for char in [';', '&', '|', '$', '`', '(', ')', '[', ']', '{', '}', '*', '?', '<', '>']):
        return {'status': 'error', 'message': 'Invalid input'}
    # Use a whitelist of allowed hosts or IP ranges
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid input'}