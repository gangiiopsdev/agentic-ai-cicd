from fastapi import FastAPI
import subprocess
import shlex
import os

class PingCommand:
    def __init__(self):
        self.safe_commands = {'ping'}

    def is_safe_command(self, command: str) -> bool:
        return command in self.safe_commands

app = FastAPI()
ping_command = PingCommand()

async def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    if not ping_command.is_safe_command('ping'):
        raise ValueError('Unsafe command detected')
    args = ['ping', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = await result.communicate()
    return {'stdout': stdout.decode(), 'stderr': stderr.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)