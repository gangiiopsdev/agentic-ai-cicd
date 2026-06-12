from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Sanitize the input to prevent command injection
        sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', self.host)
        result = await asyncio.create_subprocess_exec('ping', f'-c 1 {sanitized_host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await result.communicate()
        return stdout.decode(), stderr.decode()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):,
    validate_host(request.host)
    ping_command = PingCommand(request.host)
    status, error = ping_command.execute()
    if error:
        return {"status": "error", "error": error}
    else:
        return {"status": "completed", "stdout": status}