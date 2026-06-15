from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
    return {"status": "completed"}