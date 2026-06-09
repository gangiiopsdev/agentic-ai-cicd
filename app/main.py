from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
from shlex import quote

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', quote(self.host)]
        process = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return process.stdout

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    ping_command = PingCommand(request.host)
    result = await ping_command.execute()
    return {"status": "completed", "result": result}