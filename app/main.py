from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    validate_host(host)
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    return {"status": "completed"}