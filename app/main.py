from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get('/ping')
def ping(host: str):
    if not any(host.startswith(allowed) for allowed in ['127.0.0.1', '::1'] + [f'192.168.{i}.1' for i in range(1, 256)]) and not host.startswith('localhost'):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)