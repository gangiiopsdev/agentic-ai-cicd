from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    return {'host': host, 'status': 'Pinging'}

def validate_host(host: str) -> bool:
    # Simple validation example, replace with appropriate logic
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts