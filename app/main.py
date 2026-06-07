from fastapi import FastAPI
import asyncio
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e.stderr)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        ip_parts = host.split('')
        if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
            raise ValueError('Invalid host')
    except Exception as e:
        raise ValueError('Invalid host')
    return PingCommand(host).execute()