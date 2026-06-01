from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)