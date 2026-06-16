from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingCommand:
    def __init__(self, host: str):
        self.host = host.strip()

    async def execute(self):
        args = ['ping', '-c', '4', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return {'status': 'completed', 'output': stdout.decode(), 'error': stderr.decode()}

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    command = PingCommand(host=request.host)
    return await command.execute()