from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host.isnumeric() and int(host) < 256:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}
    return {'status': 'completed'}