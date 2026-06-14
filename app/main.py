from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using shlex.quote to prevent shell injection
        safe_host = subprocess.shlex_quote(self.host)
        await subprocess.run(['ping', safe_host], check=True)
class PingEndpoint:
    def __init__(self, app):
        self.app = app
        app.add_api_route('/ping', self.ping)

    async def ping(self, host: str):
        ping_command = PingCommand(host)
        await ping_command.execute()
app = FastAPI()
ping_endpoint = PingEndpoint(app)