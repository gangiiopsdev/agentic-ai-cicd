from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Validate the input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError('Invalid hostname')
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command)
        return result

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cmd = PingCommand(host)
    status = cmd.execute()
    return {"status": "completed"}