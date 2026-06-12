from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping(host: str):  # Secure implementation
    return {'status': await safe_ping(host)}

def is_safe_host(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']  # Define allowed hosts
    return host in allowed_hosts