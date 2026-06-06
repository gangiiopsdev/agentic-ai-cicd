from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    if not host.isalnum() or len(host) > 255:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host parameter'}
    subprocess.run(['ping'] + shlex.split(host), check=True, shell=False)
    return {'status': 'completed'}