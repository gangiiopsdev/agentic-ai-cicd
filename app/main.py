from fastapi import FastAPI
import asyncio
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        if not self.host.isdigit():
            raise ValueError('Invalid host input')
        command = ["ping", self.host]
        result = await asyncio.to_thread(subprocess.run, command, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(host)
    result = await command_executor.execute()
    return {"status": "completed", "result": result}