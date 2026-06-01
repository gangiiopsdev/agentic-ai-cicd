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

            await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()