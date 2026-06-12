from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid host'}, 400
    # Safe implementation using subprocess.run with shell=False and proper argument handling
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}