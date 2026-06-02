from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or '||' in host or ';' in host or '&' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if result['status'] == 'error':
        return result
    return {'status': 'completed'}