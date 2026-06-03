from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate the host input
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.run(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'denied'}, 403