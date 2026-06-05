from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for ping command')
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)