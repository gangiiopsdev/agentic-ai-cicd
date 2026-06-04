from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    return subprocess.call(['ping', host])

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int):
        return {'status': 'completed'}
    else:
        return result