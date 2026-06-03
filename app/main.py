from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in ['127.0.0.1', 'localhost']:
        return {'status': 'completed', 'output': ''}
    else:
        return {'status': 'failed', 'error': 'Unsafe host'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is missing'}
    result = safe_ping(host)
    return result