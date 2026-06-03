from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.run(args, shell=False)
    return {"status": "completed"}