from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await subprocess.run(['ping', self.host], check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = await command.execute()
    return {"status": "completed", "result": result.stdout.decode()}