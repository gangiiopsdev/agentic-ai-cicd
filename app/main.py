from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping'] + shlex.split(host)
    return subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid host value')
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}