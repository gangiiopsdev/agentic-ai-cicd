from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}