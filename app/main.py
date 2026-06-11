from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host not in ['localhost', '127.0.0.1']:
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}