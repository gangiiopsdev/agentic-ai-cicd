from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            return await output.stdout.read()
        except Exception as e:
            return str(e)

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it with subprocess
    if not host or not host.isalnum():
        return {'status': 'error', 'result': 'Invalid host'}
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {'status': 'completed', 'result': result}