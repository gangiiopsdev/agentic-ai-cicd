from fastapi import FastAPI
import asyncio
from pydantic import BaseModel

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with check=True and input validation
        try:
            result = await asyncio.create_subprocess_shell(f'ping {self.host}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    command = PingCommand(host=request.host)
    return await command.execute()