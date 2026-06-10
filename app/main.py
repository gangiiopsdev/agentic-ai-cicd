from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or host.strip() == 'localhost':
        return {'error': 'Invalid or restricted host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}