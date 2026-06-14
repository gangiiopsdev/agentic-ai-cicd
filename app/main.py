from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    command = PingCommand(host)
    result = await command.execute()
    output, _ = await result.communicate()
    return {'status': 'completed', 'output': output.decode('utf-8')}

def valid_host(host):
    # Add validation logic here to ensure the host is safe
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None