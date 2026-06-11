from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}