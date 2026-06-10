from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return (await result.stdout.read()).decode()

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global ping_command
    ping_command.host = host
    result = ping_command.execute()
    if '127.0.0.1' not in result and 'localhost' not in result:
        return {'status': 'Unauthorized access attempt detected', 'error': 'Access denied'}
    else:
        return {'status': result}