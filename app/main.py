from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return '127.0.0.1' in host or 'localhost' in host

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}