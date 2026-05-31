from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}