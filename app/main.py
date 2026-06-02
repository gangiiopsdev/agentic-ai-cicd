from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 64

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid input for host'}

    try:
        subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr)}

    return {'status': 'completed'}