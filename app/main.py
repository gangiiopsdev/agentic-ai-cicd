from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Secure implementation using subprocess.run with shell=False and proper argument passing
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return await result.communicate()

global_ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_ping_command.host = host
    output, error = await global_ping_command.execute()
    status = 'completed' if result.returncode == 0 else 'failed'
    return {"status": status, "output": output.decode('utf-8'), "error": error.decode('utf-8')}