from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    parsed_host = urlparse(host)
    if not parsed_host.hostname or not all([parsed_host.scheme, parsed_host.netloc]):
        return {"status": "error", "message": "Invalid host provided"}
    command_executor = PingCommand(parsed_host.hostname)
    result = await command_executor.execute()
    return {"status": "completed", "result": result.stdout.decode() if result.returncode == 0 else result.stderr.decode()}