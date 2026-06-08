from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        # Use subprocess.run instead of subprocess.call with shell=True
        result = await subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout
class PingRouter:
    def __init__(self):
        self.ping_command = PingCommand()

    async def ping(self):
        # Use the PingCommand class to execute the ping command securely
        status = await self.ping_command.execute()
        return {'status': 'completed', 'output': status}
app = FastAPI()
ping_router = PingRouter()
@app.get("/ping")
def ping(host: str):
    # Use the PingRouter class to handle the ping command securely
    result = await ping_router.ping()
    return result