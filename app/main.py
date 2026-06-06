from fastapi import FastAPI
import subprocess
import socket

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']
ALLOWED_IPS = [socket.gethostbyname(host) for host in ALLOWED_HOSTS]

async def safe_ping(host: str):
    try:
        ip = socket.gethostbyname(host)
        if ip not in ALLOWED_IPS:
            return "Invalid host"
    except socket.gaierror:
        return "Invalid host"
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout

async def validate_host(host: str):
    if host in ALLOWED_HOSTS:
        return True
    return False

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    if await validate_host(host):
        output = await safe_ping(host)
        return {"status": "completed", "output": output}
    else:
        return {"status": "invalid host", "message": "Host is not allowed"}