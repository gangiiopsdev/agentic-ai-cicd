from fastapi import FastAPI
import subprocess
from shlex import quote

global_args = ['ping', '--']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = global_args + [quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}