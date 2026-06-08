from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')

    # Secure implementation using subprocess.run with shell=False and a list of arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}