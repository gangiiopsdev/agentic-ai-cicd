from fastapi import FastAPI
import asyncio
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            args = ['ping', *shlex.split(self.host)]
            result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():  # Basic input validation to prevent OS Command Injection
        return {'status': 'failed', 'error': 'Invalid input'}
    ping_command = PingCommand(host)
    return await ping_command.execute()