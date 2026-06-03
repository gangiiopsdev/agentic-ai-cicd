from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid hostname'}