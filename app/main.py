from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    return all(c.isalnum() or c in ('.', '-') for c in host)

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}