from fastapi import FastAPI
import asyncio
import shlex
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
def sanitize_host(host):
    return ''.join(c for c in host if c.isdigit())
security = HTTPBearer()
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            sanitized_host = sanitize_host(self.host)
            result = await asyncio.create_subprocess_exec('ping', shlex.quote(sanitized_host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isnumeric():
        raise ValueError('Invalid host')
    return PingCommand(host).execute()