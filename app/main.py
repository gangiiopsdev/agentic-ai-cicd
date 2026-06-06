from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.host = None

    async def set_host(self, host: str):
        self.host = host

    async def execute(self):
        if self.host is not None:
            try:
                result = await asyncio.create_subprocess_shell(f'ping {shlex.quote(self.host)}', capture_output=True, text=True)
                return {'status': 'completed', 'output': result.stdout}
            except Exception as e:
                return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_command = PingCommand()

@app.get("/ping")
def ping(host: str):
    asyncio.run(ping_command.set_host(host))
    return asyncio.run(ping_command.execute())