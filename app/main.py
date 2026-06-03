from fastapi import FastAPI
import asyncio
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            args = ['ping', self.host]
            output = await asyncio.create_subprocess_exec(*shlex.split(' '.join(args)), stdout=subprocess.PIPE)
            return await output.stdout.read()
        except Exception as e:
            return str(e)
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it with subprocess
    if not host or not host.isalnum():
        return {'status': 'error', 'result': 'Invalid host'}
    ping_command = PingCommand(shlex.quote(host))  # Use shlex.quote for safe quoting of shell arguments
    result = await ping_command.execute()
    return {'status': 'completed', 'result': result}