from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from shlex import quote

security = HTTPBearer()

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', quote(self.host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if '.' not in host or len(host) > 15:
        return {'status': 'failed', 'error': 'Invalid host format'}
    return PingCommand(host).execute()