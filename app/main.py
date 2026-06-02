from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}