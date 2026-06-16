from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    return host

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    # Secure implementation using subprocess.run with shell=False and appropriate arguments
    result = subprocess.run(['ping', '-c', '1', validated_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}