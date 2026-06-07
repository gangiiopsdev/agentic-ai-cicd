from fastapi import FastAPI
import subprocess
import shlex
import asyncio
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    async def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            args = shlex.split(f'ping {shlex.quote(host)}')  # Use shlex.quote to escape command arguments
            result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode != 0:
                return {'status': 'failed', 'error': error.decode()}
            else:
                return {'status': 'completed', 'output': output.decode()}
        else:
            return {'status': 'denied', 'message': 'Unauthorized host'}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.safe_ping(host)