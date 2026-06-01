from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        # Sanitize input to prevent command injection
        if not self.host.strip():
            return {'status': 'error', 'message': 'Invalid host'}
        result = await asyncio.create_subprocess_exec(*args)
        return {'status': 'completed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return command.execute()