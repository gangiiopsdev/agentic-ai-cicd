from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
domain_parts = host.split('.')
if len(domain_parts) != 4:
        raise ValueError("Invalid IP address")
subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_route(host: str):
    return ping(host)