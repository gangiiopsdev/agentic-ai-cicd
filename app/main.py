from fastapi import FastAPI
import subprocess
import socket
def validate_ip(ip: str):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
app = FastAPI()
ALLOWED_HOSTS = ['example.com', 'test.com']
ALLOWED_IPS = [socket.gethostbyname(host) for host in ALLOWED_HOSTS]
def safe_ping(host: str):
    try:
        ip = socket.gethostbyname(host)
        if not validate_ip(ip) or ip not in ALLOWED_IPS:
            return "Invalid host"
    except socket.gaierror:
        return "Invalid host"
    args = ['ping', '-c', '1', ip]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
def validate_host(host: str):
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