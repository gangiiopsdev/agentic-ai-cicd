from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host or 'localhost' in host:
        return {'status': 'completed'}
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)