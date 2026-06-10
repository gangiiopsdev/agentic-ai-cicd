from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.call(args)
    return {'status': 'completed'}