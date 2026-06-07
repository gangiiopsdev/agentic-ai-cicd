from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        raise ValueError('Invalid hostname')
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {'status': 'completed'}