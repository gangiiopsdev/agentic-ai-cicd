from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        return {'error': 'Host parameter is required'}
    args = shlex.split(f'ping {host}')
    try:
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}