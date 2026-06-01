from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize the host input
    if not host.strip().replace('.', '').isalnum() or '.' not in host:
        raise ValueError('Invalid hostname')

    PingCommand(['ping', host])
    return {'status': 'completed'}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)