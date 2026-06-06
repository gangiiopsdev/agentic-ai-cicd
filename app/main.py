from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=asyncio.subprocess.PIPE)
            stdout, stderr = await result.communicate()
            return stdout.decode(), stderr.decode()
        except Exception as e:
            return str(e), None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    stdout, stderr = ping_command.execute()
    if stderr:
        return {"status": "failed", "error": stderr.decode()}
    else:
        return {"status": "completed", "output": stdout.decode()}