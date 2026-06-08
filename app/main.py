from fastapi import FastAPI
import subprocess
from pydantic import validator
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', '--', self.host]  # Adding -- to prevent injection
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout,

class HostValidator:
    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in '.-' for c in v):
            raise ValueError('Invalid host')
        return v

def validate_host(host):
    validator = HostValidator()
    validator.validate_host(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str = Depends(validate_host)):
    command = PingCommand(host)
    output, = await command.execute()
    return {'status': 'completed', 'output': output}