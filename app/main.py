from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation to prevent command injection
    if host.strip() and all(c.isalnum() or c in ' .-!' for c in host):
        subprocess.call(['ping'] + shlex.split(host), shell=False)
    return {'status': 'completed'}