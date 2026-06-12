from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    validate_host(host)
    subprocess.run(['ping', host], check=True, shell=False)
    return {"status": "completed"}