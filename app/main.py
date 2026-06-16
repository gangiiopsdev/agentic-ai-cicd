from fastapi import FastAPI
import subprocess
import shlex
def shell_safe(command):
    return [arg for arg in shlex.split(' '.join(command)) if arg.isalnum()]

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    args = shell_safe(command)
    subprocess.call(args)
    return {'status': 'completed'}