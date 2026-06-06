from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if 'localhost' in host or '127.0.0.1' in host:
        sanitized_host = subprocess.list2cmdline([host])
        subprocess.call(['ping', sanitized_host])
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')