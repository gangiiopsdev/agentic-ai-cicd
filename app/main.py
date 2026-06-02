from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    # Safer implementation with full path and shell=False
    subprocess.run(['ping'], check=True, capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)