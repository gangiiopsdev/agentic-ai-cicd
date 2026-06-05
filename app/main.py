from fastapi import FastAPI
import asyncio
import shlex
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', shlex.quote(self.host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.replace('.', '', 3).isdigit():
        raise ValueError('Invalid host')
    return PingCommand(host).execute()