from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
            return await result.communicate()
        except Exception as e:
            return str(e)

class PingRouter(BaseModel):
    async def ping(self, host: str):
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        ping_command = PingCommand(host)
        result = await ping_command.execute()
        return {'status': 'completed', 'result': result}

app = FastAPI()
ping_router = PingRouter()

@app.get('/ping')
def ping_route(host: str):
    return ping_router.ping(host)

async def is_valid_host(host: str) -> bool:
    # Add logic to validate host, e.g., IP address format check
    return True