from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add your logic to validate the host here
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host in allowed_hosts:
        return True
    raise HTTPException(status_code=403, detail='Invalid host')

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=403, detail='Invalid host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}