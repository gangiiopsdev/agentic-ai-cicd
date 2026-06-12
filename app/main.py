from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
        return result.stdout
global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    command = PingCommand(host)
    output = await command.execute()
    return {'status': 'completed', 'output': output}