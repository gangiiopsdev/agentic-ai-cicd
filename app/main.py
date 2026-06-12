from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host.strip() in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'error': 'Invalid or restricted host'}
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}