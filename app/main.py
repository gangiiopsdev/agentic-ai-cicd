from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    valid_hosts = ['example.com', 'localhost']
    return host in valid_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}