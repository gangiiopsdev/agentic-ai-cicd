from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}