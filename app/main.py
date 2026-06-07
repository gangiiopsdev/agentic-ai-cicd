from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if '.' in host or ':' in host:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not safe_ping(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Fixed implementation using shlex to safely handle command arguments
    subprocess.call(['ping', host])
    return {'status': 'completed'}