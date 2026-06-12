from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation example: allow only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400