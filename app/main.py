from fastapi import FastAPI
import asyncio
from pydantic import BaseModel
from shlex import quote

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', '-c', '1', self.host]  # Avoid using shlex.quote here
        process = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return process.stdout
gapp = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate input to ensure it's a valid hostname or IP address
    import re
    if not re.match(r"^[a-zA-Z0-9.-]+$", request.host):
        return {'status': 'error', 'message': 'Invalid host'}
    ping_command = PingCommand(request.host)
    result = await ping_command.execute()
    return {"status": "completed", "result": result}