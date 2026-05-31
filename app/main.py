from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Unauthorized host'}, 403