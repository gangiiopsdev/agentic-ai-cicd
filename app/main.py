from fastapi import FastAPI
import subprocess
import shlex

global app
global ping

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}