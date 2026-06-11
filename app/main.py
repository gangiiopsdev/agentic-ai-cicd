from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    if not host.strip() or '\' in host or '"' in host:
        raise ValueError('Invalid input')
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    output, error = await result.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}