from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        return {'status': 'error', 'message': 'Host parameter cannot be empty.'}
    command = ['ping'] + shlex.split(host)
    try:
        subprocess.run(command, check=True, capture_output=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}