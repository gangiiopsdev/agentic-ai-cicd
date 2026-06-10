from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
from subprocess import run, PIPE

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        process = await run(['ping', self.host], stdout=PIPE, stderr=PIPE)
        return process.stdout.decode()

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    ping_command = PingCommand(request.host)
    result = await ping_command.execute()
    return {"status": "completed", "result": result}