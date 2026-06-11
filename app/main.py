from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}