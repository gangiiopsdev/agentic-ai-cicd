from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call([os.path.join(os.sep, *'bin', 'ping'), '-c', '1', host])
    return {"status": "completed"}