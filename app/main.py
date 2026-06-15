from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip() or '..' in host.split('/')):
        return {'error': 'Invalid host'}, 400
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}