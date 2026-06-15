from fastapi import FastAPI
import subprocess
import shlex
class PingClient:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        args = shlex.split(f'ping {shlex.quote(self.host)}')
        return await self.run_command(args)

    async def run_command(self, args):
        import asyncio
        process = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await process.communicate()
        if error:
            raise Exception(error.decode())
        return {'status': 'completed', 'output': output.decode()}
class FastAPIApp(FastAPI):
    def __init__(self):
        super().__init__()

app = FastAPIApp()

@app.get("/ping")
def ping(host: str):
    client = PingClient(host)
    return client.ping()