from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = set()

    def add_allowed_host(self, host):
        self.allowed_hosts.add(host)

    def ping(self, host):
        if host not in self.allowed_hosts and '@' not in host and not host.isdigit():
            # Sanitize the input to avoid shell injection
            sanitized_host = shlex.quote(host)
            args = ['ping', sanitized_host]
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