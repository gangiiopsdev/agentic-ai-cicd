from fastapi import FastAPI
import subprocess
import shlex
import os
global_args = 'ping'
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use shlex to safely split the command line
    args = shlex.split(f'{} {host}')
    if not any(os.path.exists(p) for p in [''] + args):
        return {'status': 'failed', 'error': 'Command not found'}
    try:
        result = subprocess.run([global_args] + args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}