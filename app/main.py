from fastapi import FastAPI
import os
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Use os.system instead of subprocess for simple commands that do not require capturing output
            result = await asyncio.create_task(os.system(f'ping {self.host}'))
            return {'status': 'completed', 'output': ''}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return await ping_command.execute()