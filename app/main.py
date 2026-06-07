from fastapi import FastAPI
import subprocess
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE)

class PingRequest(BaseModel):
    host: Optional[str] = None

@app.post('/ping')
def ping(request: PingRequest):
    if not request.host:
        raise HTTPException(status_code=400, detail='Host is required')
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        raise HTTPException(status_code=400, detail='Invalid host')
    ping_command = PingCommand(request.host)
    result = await ping_command.execute()
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}