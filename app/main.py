from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    ping_command = ['ping', host]
    result = subprocess.run(ping_command, capture_output=True, text=True)
    return result.stdout

class PingRouter:
    def __init__(self):
        self.app = FastAPI()
        self.app.get('/ping')(lambda: safe_ping('example.com'))
ping_router = PingRouter().app