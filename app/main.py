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

            args = ['ping', self.host]
            process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await process.communicate()
            if error:
                return {'status': 'failed', 'error': error.decode()}
            return {'status': 'completed', 'output': output.decode()}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()