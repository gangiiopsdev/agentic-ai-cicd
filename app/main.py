from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for demonstration purposes
        subprocess.call(['ping', host])
    else:
        raise ValueError('Ping to non-localhost hosts is not allowed')

@app.get("/ping")
def ping(host: str):
    if host in ['127.0.0.1', '::1']:
        subprocess.call(['ping', host])  # Safe as it only allows localhost
    else:
        raise ValueError('Ping to non-localhost hosts is not allowed')
    return {"status": "completed"}