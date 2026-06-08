from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        return {'error': 'Invalid characters in hostname'}
    args = shlex.split(f'ping -c 4 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}