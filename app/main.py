from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with args instead of shell=True and proper argument handling
    if not isinstance(host, str) or len(host.strip()) == 0:
        raise ValueError("Invalid host")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}