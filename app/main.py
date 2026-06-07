from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    subprocess.call(command)
    return {'status': 'completed'}