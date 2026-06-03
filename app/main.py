from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isdigit():
        return subprocess.call(['ping', '-c', '1', host]) == 0
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    try:
        return {'status': 'completed' if safe_ping(host) else 'failed'}
    except Exception as e:
        return {'error': str(e)}