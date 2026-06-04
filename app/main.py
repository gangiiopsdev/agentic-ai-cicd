from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        await asyncio.create_subprocess_exec('ping', self.host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain any malicious content
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    ping_command = PingCommand(host)
    await ping_command.execute()
    return {'status': 'completed'}