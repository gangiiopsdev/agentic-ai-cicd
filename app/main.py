from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

@app.get("/ping")
def ping(host: str):
    if host and '@' not in host and ':' not in host and '/' not in host:
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid hostname'}