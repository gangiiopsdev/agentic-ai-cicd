from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    ping_command = ['ping', shlex.quote(host)]
    subprocess.run(ping_command, check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return run_ping(host)