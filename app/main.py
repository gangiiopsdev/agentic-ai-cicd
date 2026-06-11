from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}