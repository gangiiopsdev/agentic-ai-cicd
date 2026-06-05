from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation for demonstration purposes
    allowed_hosts = ['google.com', 'example.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    validate_host(host)
    subprocess.call(['ping', host])
    return {"status": "completed"}