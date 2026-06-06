from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.run(args, check=True)  # Use subprocess.run instead of subprocess.call for better security
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400