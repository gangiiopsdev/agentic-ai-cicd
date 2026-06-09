from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if all(c.isalnum() or c in '-.' for c in host) and len(host.split('.')) == 4:
        return subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host address')

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}