from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']

@app.get('/ping')
def ping(host: str):
    if host in allowed_hosts:
        subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}