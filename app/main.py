from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'another-example.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}