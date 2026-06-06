from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'invalid_host'}
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {'status': 'completed'}