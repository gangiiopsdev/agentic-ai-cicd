from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if sanitize_input(host):
        subprocess.call(['ping', '--', host])  # Use '--' to prevent command injection
    return {'status': 'completed'}