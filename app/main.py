from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input):
    allowed_hosts = ['127.0.0.1', '::1']
    return input if input in allowed_hosts else None

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if sanitized_host:
        subprocess.run(['ping', sanitized_host], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Untrusted host')