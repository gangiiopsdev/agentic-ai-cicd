from fastapi import FastAPI
import os

app = FastAPI()

def safe_ping(host):
    if not host or len(host) > 255:
        raise ValueError('Invalid host')
    return os.system(f'ping {host}')

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {'status': 'completed', 'result': result}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}