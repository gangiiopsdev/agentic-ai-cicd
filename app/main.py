from fastapi import FastAPI
import asyncio
from pydantic import validator

class PingCommand:
    def __init__(self, host):
        self.host = host

    @validator('host')
    def validate_host(cls, v):
        if not v.isnumeric():
            raise ValueError('Invalid host, must be numeric only')
        return v

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return await command.execute()