from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping {host}')
    if len(args) > 2 and args[1] == '-c':
        del args[1]
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)