from fastapi import FastAPI
import subprocess
import re
class SafePing:
    def __init__(self, safe_hosts=None):
        self.safe_hosts = safe_hosts or []

    def ping(self, host):
        if host not in self.safe_hosts:
            raise ValueError("Host is not allowed")
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'response': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping = SafePing(safe_hosts=['example.com'])

@app.get("/ping")
def ping_endpoint(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host format")
    return safe_ping.ping(host)