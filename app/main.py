from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get="/ping")
def ping(host: str):
    # Secure implementation
    validate_host(host)
    subprocess.call(['ping', host])
    return {"status": "completed"}