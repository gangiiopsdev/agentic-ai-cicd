from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Safe implementation
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE)
        output, _ = await result.communicate()
        return output.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    status = await command.execute()
    return {"status": status}