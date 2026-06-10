from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> bool:
    return all(c.isalnum() or c in '.-' for c in host)

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'invalid host'}
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}