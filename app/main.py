from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))
    return {'status': 'completed'}