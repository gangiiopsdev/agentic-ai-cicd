from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize input
    domain_parts = host.split('.')
    if len(domain_parts) != 4:
        raise ValueError("Invalid IP address")
    subprocess.run(['ping', '-c', '1', host], check=True)

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    return ping(host)