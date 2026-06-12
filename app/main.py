from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['localhost']
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not sanitize_host(host):
        return {'error': 'Invalid or restricted host'}
    try:
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e}'}