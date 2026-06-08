from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        result = await subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)
        return result.stdout

global_ping_command = PingCommand(host='example.com')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = global_ping_command.ping()
    return {"status": "completed", "output": result}