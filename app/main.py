from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not isinstance(host, str) or not host.strip().replace('.', '').isdigit() or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid IP address'}
    return safe_ping(host)