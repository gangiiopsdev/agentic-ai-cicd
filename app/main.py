from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}