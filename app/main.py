from fastapi import FastAPI
import subprocess
from ipaddress import ip_address, IPv4Address, IPv6Address
global allow_ping_hosts = set(['127.0.0.1', '::1'])

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ip_address(host)
        if host in allow_ping_hosts:
            result = subprocess.call(['ping', '-c', '1', host], shell=False, executable='/bin/bash')
            return {"status": "completed", "result": result == 0}
        else:
            return {"status": "error", "message": "Invalid host"}
    except ValueError:
        return {"status": "error", "message": "Invalid IP address"}