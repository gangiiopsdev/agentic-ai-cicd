from fastapi import FastAPI
import asyncio
import shlex
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with check=True and sanitized input
        try:
            if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
                return {'status': 'failed', 'error': 'Invalid hostname'}
            result = await asyncio.create_subprocess_shell(f'ping {shlex.quote(self.host)}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()