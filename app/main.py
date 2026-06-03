from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    try:
        args = ['ping'] + [shlex.quote(arg) for arg in host.split()]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

global app
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip():
        raise ValueError('Invalid host input')
    status = safe_ping(host)
    return {'status': 'completed', 'result': status}