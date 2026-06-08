from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', '192.168.1.1']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', '-c', '4', host], check=True)
    else:
        raise ValueError('Invalid host')

    return {"status": "completed"}