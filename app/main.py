from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    # Use a whitelist of allowed hosts or validate the input more strictly
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', shlex.quote(host)], check=True, shell=False)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)