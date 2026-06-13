from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)