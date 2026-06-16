from fastapi import FastAPI
import subprocess
import re
import asyncio

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Secure implementation with validation and sanitization
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError("Invalid hostname")
        await asyncio.create_subprocess_exec('ping', self.host)

async def ping(host: str):
    ping_command = PingCommand(host)
    # Execute the ping command securely
    await ping_command.execute()
    return {"status": "completed"}
global app
app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    return await ping(host)