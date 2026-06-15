from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', '-c', '1', self.host], stderr=subprocess.STDOUT)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'error': e.output.decode('utf-8')}

class PingRouter:
    def __init__(self):
        self.ping_command = PingCommand(None)

    async def ping(self, host: str):
        self.ping_command.host = host
        return await self.ping_command.execute()

app = FastAPI()
ping_router = PingRouter()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping_router.ping(host)