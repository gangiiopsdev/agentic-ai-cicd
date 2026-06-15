from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using shlex.quote to prevent shell injection
        safe_host = subprocess.shlex_quote(self.host)
        await asyncio.create_subprocess_exec('ping', safe_host)
class PingEndpoint:
    def __init__(self, app):
        self.app = app
        app.add_api_route('/ping', self.ping)

    async def ping(self, host: str):
        # Input validation and sanitization
        if not host or len(host) > 255 or not all(c.isalnum() for c in host):
            raise ValueError('Invalid host name')
        ping_command = PingCommand(host)
        await ping_command.execute()
app = FastAPI()
ping_endpoint = PingEndpoint(app)