from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    validate_host(host)
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {"status": "completed"}