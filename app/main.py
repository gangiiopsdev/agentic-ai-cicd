from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str):
        return {'error': 'Invalid input'}
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}