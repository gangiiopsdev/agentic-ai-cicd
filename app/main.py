from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == '127.0.0.1':
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Invalid host'}