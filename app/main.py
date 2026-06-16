from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        if not all(arg.isalnum() for arg in args):
            return {'status': 'failed', 'error': 'Invalid input'}
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}