from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    def safe_ping(self, host: str):
        if not host.isalnum():
            raise ValueError('Invalid input')
        args = [self.ping_command] + shlex.split(host)
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout
class PingEndpoint:
    def __init__(self, safe_ping_instance: SafePing):
        self.safe_ping_instance = safe_ping_instance

    @app.get("/ping")
    def ping(self, host: str):
        try:
            return self.safe_ping_instance.safe_ping(host)
        except ValueError as e:
            return {'error': str(e)}, 400