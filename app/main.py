from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host or '"' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if 'error' in result:
        return result
    else:
        return {'status': 'completed'}