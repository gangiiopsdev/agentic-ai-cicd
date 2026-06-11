from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}