from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        await asyncio.create_subprocess_exec('ping', self.host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    safe_host = subprocess.quote(host)
    ping_command = PingCommand(safe_host)
    await ping_command.execute()
    return {"status": "completed"}