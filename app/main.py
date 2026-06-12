from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host.strip() == 'localhost' or '127.0.0.1':
        command = ['ping', shlex.quote(host)]
        subprocess.call(command, shell=False)
    else:
        return {'status': 'error', 'message': 'Unsafe host'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    return {'status': 'completed'}