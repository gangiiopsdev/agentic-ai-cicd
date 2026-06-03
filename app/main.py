from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_shell(
                f'ping {shlex.quote(self.host)}',
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
class PingRouter:
    def __init__(self):
        self.ping_command = PingCommand(host='example.com')

    async def ping(self):
        return await self.ping_command.execute()

app = FastAPI()
ping_router = PingRouter()

@app.get('/ping')
def ping_route():
    return ping_router.ping()