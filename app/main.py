from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host in ['127.0.0.1', 'localhost']:
        subprocess.run(['ping', host], check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)