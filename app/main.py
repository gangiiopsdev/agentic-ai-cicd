from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isdigit():
        args = ['ping', '-c', '1', host]
        return subprocess.call(args) == 0
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        return {'status': 'completed' if safe_ping(host) else 'failed'}
    except Exception as e:
        return {'error': str(e)}