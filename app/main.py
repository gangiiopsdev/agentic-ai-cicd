from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with args and validation
        if not self.host or len(self.host) > 255:
            raise ValueError('Invalid host input')
        await subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    await command.execute()
    return {"status": "completed"}