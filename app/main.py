from fastapi import FastAPI
import asyncio
from sanic.response import json
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Use a whitelist of allowed hosts to prevent command injection
            allowed_hosts = ['example.com', 'test.com']
            if not self.host or self.host not in allowed_hosts:
                return json({'error': 'Invalid host'}, status=400)

            # Sanitize the input before using it in subprocess execution
            sanitized_host = self._sanitize_host(self.host)
            await asyncio.create_subprocess_exec('ping', sanitized_host, stdout=subprocess.PIPE)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

    def _sanitize_host(self, host):
        # Implement a proper sanitization method here
        import re
        allowed_chars = r'^[a-zA-Z0-9.-]+$'
        if not re.match(allowed_chars, host):
            raise ValueError('Invalid characters in host')

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()