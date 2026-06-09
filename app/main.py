from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode(), stderr.decode()

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    ping_command = PingCommand(request.host)
    status, error = ping_command.execute()
    if error:
        return {"status": "error", "error": error}
    else:
        return {"status": "completed", "stdout": status}