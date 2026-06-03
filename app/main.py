from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation: allow only alphanumeric characters and some common delimiters
    return all(c.isalnum() or c in ['.', '-', '_'] for c in host)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Invalid host input'}, 400