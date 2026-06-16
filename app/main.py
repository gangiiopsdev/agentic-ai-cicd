from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])
app = FastAPI()
@app.get('/ping')
def ping_safe(host: str):
    return {'host': host, 'result': ping(host)}