from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess safely by limiting inputs and validating
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        subprocess.call(['ping', host])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}