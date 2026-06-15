from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Secure implementation with validation and sanitization
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError("Invalid hostname")
        await asyncio.create_subprocess_exec('ping', self.host)

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    # Execute the ping command securely
    asyncio.run(ping_command.execute())
    return {"status": "completed"}