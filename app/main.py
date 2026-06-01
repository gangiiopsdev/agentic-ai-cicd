from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        return {'error': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True)
    return {'status': 'completed'}