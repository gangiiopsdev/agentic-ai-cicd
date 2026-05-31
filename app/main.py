from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host or 'ipconfig' in host:
        raise ValueError('Invalid input for ping')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}