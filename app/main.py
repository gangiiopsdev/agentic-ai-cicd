from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        args = ['ping', host]
        if subprocess.call(shlex.split(' '.join(args)), check=True) == 0:
            return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get("/ping")
def ping(host: str):
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):  # Basic validation
        return {'error': 'Invalid host'}
    return safe_ping(host)