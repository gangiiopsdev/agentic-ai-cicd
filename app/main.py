from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}