from fastapi import FastAPI
import subprocess

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']

@app.get('/ping')
def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}