from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if host.strip() in ['localhost', '127.0.0.1']:
        command = ['ping', shlex.quote(host)]
        subprocess.run(command, shell=False)
    else:
        return {'status': 'error', 'message': 'Unsafe host'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    return {'status': 'completed'}