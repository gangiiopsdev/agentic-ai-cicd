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
    return safe_ping(host)