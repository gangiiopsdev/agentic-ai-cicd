from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}