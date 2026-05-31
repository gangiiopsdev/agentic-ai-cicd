from fastapi import FastAPI
import subprocess
from sanic.response import json
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Sanitize the input to prevent command injection
            if not self.host or not isinstance(self.host, str) or ' ' in self.host:
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