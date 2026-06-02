from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.valid_hosts = ['example.com', 'localhost']

    def ping(self, host: str) -> dict:
        if host not in self.valid_hosts:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=10)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}
class SafePingEndpoint:
    def __init__(self):
        self.safe_ping = SafePing()

    @app.get("/ping")
    def ping(self, host: str):
        return self.safe_ping.ping(host)