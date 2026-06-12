from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], shell=False, check=True)
    return {'status': 'completed'}