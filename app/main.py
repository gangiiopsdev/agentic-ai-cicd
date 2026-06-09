from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, check=True, text=True, shell=False)
    if result.returncode == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': result.stderr}

@app.get('/ping')
def ping_safe(host: str):
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, check=True, text=True, shell=False)
    if result.returncode == 0:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': result.stderr}