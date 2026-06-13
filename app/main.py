from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Add your validation logic here, e.g., whitelist allowed hosts
    return host in ['host1', 'host2']

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}