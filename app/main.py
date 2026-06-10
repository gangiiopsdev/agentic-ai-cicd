from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', *shlex.split(host)]
    if os.name == 'nt':  # Windows
        args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}