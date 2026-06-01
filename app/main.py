from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_endpoint(host: str):
    return {'status': 'Pinging ' + host}