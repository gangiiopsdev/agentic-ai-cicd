from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', '1', os.path.realpath(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)