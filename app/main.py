from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return 'localhost' in host or '127.0.0.1' in host

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}