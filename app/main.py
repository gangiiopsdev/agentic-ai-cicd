from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}