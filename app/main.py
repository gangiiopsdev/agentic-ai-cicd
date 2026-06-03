from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with input validation
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}