from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    output = secure_ping(host)
    return {'status': 'completed', 'output': output}