from fastapi import FastAPI
import subprocess
import shlex

global host
host = 'example.com'

app = FastAPI()

@app.get('/ping')
def ping():
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

    return {'status': 'completed'}