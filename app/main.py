from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'reason': 'Invalid host input'}
    command = ['ping', '-c', '1', host]
    subprocess.run(command, check=True, capture_output=True)
    return {'status': 'completed'}