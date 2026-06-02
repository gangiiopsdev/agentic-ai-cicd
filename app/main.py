from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or host not in ['127.0.0.1', '::1']:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except Exception as e:
        return {'error': str(e)}