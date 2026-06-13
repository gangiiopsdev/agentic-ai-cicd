from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        cmd = shlex.split(command)
        return subprocess.run(cmd, *args, **kwargs)

app = FastAPI()

async def ping(host: str):
    # Safe implementation
    if not host.isalnum():  # Basic validation for alphanumeric characters only
        raise ValueError('Invalid host name')
    safe_command = f'ping {shlex.quote(host)}'
    await SafeSubprocess.call(safe_command)

@app.get("/ping")
def ping_route(host: str):
    return {'code': 'success', 'message': 'Ping sent successfully'}