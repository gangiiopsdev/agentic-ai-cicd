from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host.isnumeric() or '.' in host:
        return subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'error': str(e)}