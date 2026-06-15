from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['google.com', 'example.com']

def validate_host(host):
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}, 400
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}