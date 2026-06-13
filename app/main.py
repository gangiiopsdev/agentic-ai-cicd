from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Add your allowed hosts here
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}