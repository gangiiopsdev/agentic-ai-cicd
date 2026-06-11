from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.call(['ping', '-c 1', subprocess.list2cmdline([host])])
    return {'status': 'completed'}