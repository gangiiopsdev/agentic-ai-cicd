from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)