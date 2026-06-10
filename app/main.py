from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', shlex.quote(host)]
    if subprocess.call(args) != 0:
        raise Exception('Ping failed')

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}