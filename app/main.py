from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, capture_output=True, text=True)
            return (await result.stdout.read()).decode()
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.output.decode()}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    status = await ping_command.execute()
    return {'status': status}