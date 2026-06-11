from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
def quote_host(host):
    return ''.join(c if c.isalnum() or c in ['.', '-', '_'] else '_' for c in host)
class PingCommand:
    def __init__(self, host):
        self.host = quote_host(host)

    async def execute(self):
        args = ['ping', '-c', '1', self.host]
        process = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return process.stdout
gapp = FastAPI()
class PingRequest(BaseModel):
    host: str
@app.get("/ping")
def ping(request: PingRequest):
    ping_command = PingCommand(request.host)
    result = await ping_command.execute()
    return {"status": "completed", "result": result}