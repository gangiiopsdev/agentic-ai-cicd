from fastapi import FastAPI
import re
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = {'safehost1', 'safehost2'}

    def is_safe_host(self, host):
        return host in self.safe_hosts

app = FastAPI()
ping_service = SafePing()

@app.get('/ping')
def ping(host: str):
    if ping_service.is_safe_host(host):
        subprocess.call(shlex.split(f'ping {host}'))
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 403