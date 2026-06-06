from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.strip() and '@' not in host:
        args = shlex.split('ping ' + host)
        subprocess.call(args, shell=False)
    else:
        raise ValueError('Invalid hostname provided')
    return {'status': 'completed'}