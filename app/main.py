from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):

    if not validate_host(host):
        raise ValueError('Invalid host')

    # Secure implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}