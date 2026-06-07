from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', *shlex.split(host)]
    subprocess.call(args, shell=False)

@app.get('/ping')
def ping_safe(host: str):
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True, text=True)
    return {'status': 'completed'}