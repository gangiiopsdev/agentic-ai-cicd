from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            # Use shlex.quote to safely escape the host parameter
            await asyncio.create_subprocess_exec('ping', shlex.quote(self.host), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    return await ping_command.execute()