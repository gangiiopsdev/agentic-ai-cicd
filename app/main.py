from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'localhost']

    def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Unauthorized host')
        safe_host = shlex.quote(host)
        subprocess.call(['ping', safe_host])
class PingRouter:
    def __init__(self, pinger: SafePinger):
        self.pinger = pinger

    @app.get('/ping')
    def ping(self, host: str):
        return {'status': 'completed', 'response': self.pinger.ping(host)}
pinger = SafePinger()
ping_router = PingRouter(pinger)