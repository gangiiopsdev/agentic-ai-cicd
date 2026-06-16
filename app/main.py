from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if '.' in host and ':' not in host:
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host format')

@app.get("/ping")
def ping(host: str):
    try:
        return {'status': safe_ping(host)}
    except Exception as e:
        return {'error': str(e)}, 400