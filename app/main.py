from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'error': str(e)}