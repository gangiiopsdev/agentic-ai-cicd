from fastapi import FastAPI
import subprocess
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
    command_executor = PingCommand(host)
    result = await command_executor.execute()
    return {"status": "completed", "result": result.stdout.decode() if result.returncode == 0 else result.stderr.decode()}