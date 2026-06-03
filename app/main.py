from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isnumeric():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))
    return {'status': 'completed'}