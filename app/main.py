from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    if validate_host(host):
        subprocess.run(['ping', host], check=True)\n    return {"status": "completed"}