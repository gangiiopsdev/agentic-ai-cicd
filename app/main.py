from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host != '127.0.0.1':
        return {'error': 'Invalid host'}
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}