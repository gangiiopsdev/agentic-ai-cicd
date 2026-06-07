from fastapi import FastAPI
import subprocess
import shlex
import ipaddress

app = FastAPI()

def is_valid_ip(ip):
    try:
        return ipaddress.ip_address(ip)
    except ValueError:
        return False

@app.get("/ping")
def ping(host: str):
    if not is_valid_ip(host):
        raise ValueError("Invalid IP address")
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)

    return {"status": "completed"}