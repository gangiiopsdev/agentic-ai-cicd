from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping_route(host: str):
    if validate_host(host):
        return ping(host)
    else:
        return {'error': 'Invalid host'}, 400