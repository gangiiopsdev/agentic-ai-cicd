from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip().endswith('ping') or host.strip() == 'localhost':
        return False
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}