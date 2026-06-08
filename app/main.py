from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip() or not all(c.isalnum() or c in ('.', '-') for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}