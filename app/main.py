from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    return False

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host provided')
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}