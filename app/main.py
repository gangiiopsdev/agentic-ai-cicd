from fastapi import FastAPI
import re
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Regular expression to validate allowed hosts
        if re.match(r'^example\.com|test\.com$', self.host):
            args = ['ping', self.host]
            result = await asyncio.create_subprocess_exec(*args)
            return await result.wait()
        else:
            raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    await command.execute()
    return {'status': 'completed'}