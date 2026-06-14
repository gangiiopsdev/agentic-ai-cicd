from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Subprocess failed with error code {e.returncode}'}, 500
    return {'status': 'completed'}