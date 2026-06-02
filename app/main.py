from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized host')

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}