from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}