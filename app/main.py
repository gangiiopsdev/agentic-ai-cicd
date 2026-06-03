from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        return subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Ping to external hosts is not allowed')

@app.get('/ping')
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': result.stdout}
    except ValueError as e:
        return {'error': str(e)}