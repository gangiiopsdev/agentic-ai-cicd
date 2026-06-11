from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement logic to validate the host input
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'error': 'Invalid host'}
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}