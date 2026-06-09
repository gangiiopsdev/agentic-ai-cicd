from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', '-c', '4', host], check=True, shell=False)
    else:
        raise ValueError('Invalid host')

    return {"status": "completed"}