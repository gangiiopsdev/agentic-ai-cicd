from fastapi import FastAPI
import subprocess
import shlex
import re

class SafePing:
    def __init__(self):
        self.allowed_hosts = set()

    def add_allowed_host(self, host):
        if re.match(r'^[a-zA-Z0-9.-]+$', host):
            self.allowed_hosts.add(host)

    def ping(self, host):
        if host not in self.allowed_hosts and '@' not in host and not host.isdigit():
            args = ['ping', host]
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        else:
            return 'Invalid input'

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/add_host")
def add_host(host: str):
    safe_ping_instance.add_allowed_host(host)
    return {"message": "Host added to allowed list"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping_instance.ping(host)
    return {"status": "completed", "response": response}