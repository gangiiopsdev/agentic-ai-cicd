from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def run(self):
        args = ['ping', self.host]
        await asyncio.create_subprocess_exec(*args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    await ping_command.run()
    return {"status": "completed"}