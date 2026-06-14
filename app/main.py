from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add your logic to validate the host
    allowed_hosts = ['safehost1.com', 'safehost2.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}, 403