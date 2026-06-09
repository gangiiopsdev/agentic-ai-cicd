from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    if not all(part.isalnum() or part in '-.' for part in host.split()):
        raise ValueError('Invalid characters in hostname')
    if subprocess.call(args) != 0:
        raise Exception('Ping failed')

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}