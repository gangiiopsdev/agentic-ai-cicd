from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    try:
        subprocess.call(['ping', host], shell=False)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

    return {'status': 'completed'}