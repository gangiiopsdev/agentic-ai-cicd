from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Input validation and sanitization
    if not host.strip() or '.' not in host:
        return False
    # Use a whitelist of allowed hosts
    allowed_hosts = ['8.8.8.8', '192.168.1.1']  # Example list, replace with actual allowed hosts
    if host in allowed_hosts:
        return True
    else:
        return False
class PingEndpoint:
    def __init__(self):
        self.app = FastAPI()
    @app.get('/ping')
    def ping(self, host: str):
        if safe_ping(host):
            subprocess.call(['ping', host], shell=False)
            return {'status': 'completed'}
        else:
            return {'status': 'invalid input'}