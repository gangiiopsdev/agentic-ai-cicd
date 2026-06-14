from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}