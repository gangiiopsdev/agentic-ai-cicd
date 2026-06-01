from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = ['ping', quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}