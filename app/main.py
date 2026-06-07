from fastapi import FastAPI
import asyncio
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        # Validate the host input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError('Invalid host format')
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    result = await PingCommand(host).run()
    return {"status": "completed", "stdout": result.stdout.decode('utf-8'), "stderr": result.stderr.decode('utf-8')}