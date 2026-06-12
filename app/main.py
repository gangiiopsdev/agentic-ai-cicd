from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):  # Allow only local host
        args = ['ping', shlex.quote(host)]
        subprocess.call(args)
    return {'status': 'completed'}