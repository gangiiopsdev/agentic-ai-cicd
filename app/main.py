from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command_parts):
        self.command_parts = command_parts

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec(*self.command_parts, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Command failed: {e}

class PingHandler:
    @staticmethod
    async def ping(host: str):
        command_parts = ['ping', '--', host]  # Use -- to prevent option injection
        handler = PingCommand(command_parts)
        return {'status': 'completed', 'output': await handler.execute()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return PingHandler.ping(host)