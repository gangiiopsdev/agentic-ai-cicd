from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, text=True)

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}