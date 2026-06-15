from fastapi import FastAPI
import re
import subprocess

class FastAPISafePing(FastAPI):
    @app.get("/ping")
    async def ping(self, host: str):
        if not host.strip() or host.strip().endswith(' '):
            raise ValueError('Invalid host value')
        # Use regular expression to ensure the host is a valid hostname/IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host value')
        # Sanitize the host input using subprocess.quote instead of shlex.quote
        args = ['ping', subprocess.quote(host)]
        result = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode().strip()}

app = FastAPISafePing()