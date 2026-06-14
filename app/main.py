from fastapi import FastAPI
import subprocess
import shlex

global ALLOWED_HOSTS = ['example.com', 'test.com']

app = FastAPI()

def ping(host: str):
    if host not in ALLOWED_HOSTS:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split('ping ' + host)
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)