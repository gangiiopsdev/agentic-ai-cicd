from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(hostname):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Add more valid hosts if needed
    if hostname not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_route(host: str):
    validate_host(host)
    return ping(host)