from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        try:
            result = await subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host=host)
    result = await command.ping()
    return {"status": "completed", "output": result}