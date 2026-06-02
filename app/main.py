from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    validate_host(host)
    try:
        subprocess.run(["ping", '-c', '1', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}