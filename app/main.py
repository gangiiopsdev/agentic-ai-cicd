from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.call(args, *args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Fixed implementation
    command = f'ping {host}'
    return SafeSubprocess.call(command)