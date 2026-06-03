from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    try:
        sanitize_host(host)
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}