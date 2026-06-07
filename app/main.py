from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    args = ["ping", host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}