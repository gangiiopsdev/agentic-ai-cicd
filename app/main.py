from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if host.strip() != host or host.startswith('-'):  # Basic validation example
        raise ValueError('Invalid host name')
    subprocess.call(['ping'] + shlex.split(host), shell=False)
    return {'status': 'completed'}