from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Basic validation example: allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}