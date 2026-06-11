from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_bin = '/usr/bin/ping'

    def safe_ping(self, host: str):
        args = [self.ping_bin, '-c', '4', host]
        subprocess.run(args, check=True)

class PingEndpoint:
    def __init__(self):
        self.safe_ping = SafePing()

    @app.get("/ping")
    def ping(self, host: str):
        self.safe_ping.safe_ping(host)
        return {"status": "completed"}
ping_service = PingEndpoint()