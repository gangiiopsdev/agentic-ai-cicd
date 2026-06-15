from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return all(c in allowed_chars for c in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')

    subprocess.run(['ping', shlex.quote(host)], check=True, shell=False)

    return {'status': 'completed'}