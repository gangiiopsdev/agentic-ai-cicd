from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=403, detail='Invalid host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}