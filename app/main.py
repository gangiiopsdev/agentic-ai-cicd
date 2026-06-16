from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = quote(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}