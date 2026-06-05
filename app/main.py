from fastapi import FastAPI
import subprocess
import re
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = ['ping']

    async def ping(self, host: str):
        if re.match(r'^[a-zA-Z0-9.-]+$', host):
            safe_host = shlex.quote(host)
            full_command = self.ping_command + [safe_host]
            subprocess.call(full_command, shell=False)
        else:
            raise ValueError('Invalid input for host')
class PingRouter:
    def __init__(self):
        self.safe_ping = SafePing()

    @app.get('/ping')
    async def ping(self, host: str):
        await self.safe_ping.ping(host)

router = PingRouter()