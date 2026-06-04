from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}