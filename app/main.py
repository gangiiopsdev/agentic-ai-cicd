from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Simple example of validation
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}