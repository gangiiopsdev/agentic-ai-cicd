from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use shlex to safely split the command line
    args = shlex.split(f'ping {host}')
    if not any(os.path.exists(p) for p in ['ping'] + args):
        return {'status': 'failed', 'error': 'Command not found'}
    try:
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}