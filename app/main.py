from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual safe hosts
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise HTTPException(status_code=400, detail='Invalid host')
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}