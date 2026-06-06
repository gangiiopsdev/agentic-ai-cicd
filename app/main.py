from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400

    # Safe implementation
    subprocess.call(['ping', host], shell=False)

    return {'status': 'completed'}