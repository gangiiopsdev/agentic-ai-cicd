from fastapi import FastAPI
import subprocess
import shlex
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}