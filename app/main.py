from fastapi import FastAPI
import asyncio
import shlex
class SafePing:
    def __init__(self):
        self.command = ['ping']

    async def ping_host(self, host: str) -> dict:
        if not host:
            return {'error': 'Host parameter is required'}
        command_parts = shlex.split(' '.join(self.command + [host]))
        result = await asyncio.create_subprocess_exec(*command_parts,
                                             capture_output=True,
                                             text=True)
        output = await result.stdout.read()
        return {'status': 'completed', 'output': output}

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'error': 'Host parameter is required'}
    return safe_ping.ping_host(host)