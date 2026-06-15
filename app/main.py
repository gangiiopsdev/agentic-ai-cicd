from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)