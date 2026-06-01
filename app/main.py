from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement host validation logic here
    return '.' in host

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}