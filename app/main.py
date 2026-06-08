from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
        return await result.communicate()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    ping_command = PingCommand(sanitized_host)
    output, _ = await ping_command.execute()
    return {"status": "completed", "output": output.decode()}