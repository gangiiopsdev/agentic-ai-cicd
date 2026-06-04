from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or ' ' in host:
        raise ValueError('Invalid host provided')
    args = shlex.split('ping ' + shlex.quote(host))
    subprocess.call(args)

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)