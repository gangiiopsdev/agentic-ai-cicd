from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Simple validation example; in production use a more robust method
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get="/ping")
def ping(host: str):
    validate_host(host)
    command = ["ping", host]
    subprocess.call(command)
    return {"status": "completed"}