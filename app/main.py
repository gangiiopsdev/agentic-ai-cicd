from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()
class PingRequest(BaseModel):
    host: str
class PingEndpoint:
    def __init__(self):
        pass

    async def ping(self, request: PingRequest):
        output, error = await PingCommand(request.host).execute()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
global app
app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    endpoint = PingEndpoint()
    return endpoint.ping(request)