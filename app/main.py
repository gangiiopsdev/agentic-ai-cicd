from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Sanitize input before passing to subprocess
        if not self.host.isalnum():
            raise ValueError('Invalid hostname')
        return await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ping_command = PingCommand(host)
        result, _ = await ping_command.execute()
        return {'status': 'completed', 'result': result.decode()}
    except ValueError as e:
        return {'error': str(e)}