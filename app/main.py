from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    return ''.join(filter(str.isalnum, host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ["ping", sanitized_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}