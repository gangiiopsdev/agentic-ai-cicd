from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isnumeric():
        return subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host address')

@app.get="/ping")
def ping(host: str):
    return {'status': safe_ping(host)}