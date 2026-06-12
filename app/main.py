from fastapi import FastAPI
import subprocess
import shlex

class SanitizedSubprocess:
    @staticmethod
def run(command: str):
        args = shlex.split(command)
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host or not isinstance(host, str) or ' ' in host:
        raise ValueError('Invalid host value')
    SanitizedSubprocess.run(f'ping {host}')
    return {"status": "completed"}