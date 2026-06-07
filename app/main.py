from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host parameter
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'reason': 'Invalid hostname'}
    subprocess.call(['ping', shlex.quote(host)])
    return {'status': 'completed'}