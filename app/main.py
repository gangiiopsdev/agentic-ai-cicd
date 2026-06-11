from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    safe_ping = SafePing(host)
    subprocess.run(['ping', safe_ping.host], check=True)