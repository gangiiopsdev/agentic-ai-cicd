from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation (e.g., allow only alphanumeric characters and hyphens)
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host name")

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host])
    return {'status': 'completed'}