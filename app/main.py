from fastapi import FastAPI
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        args = ['ping', self.host]
        # Use a whitelist of allowed hosts to mitigate risks
        if self.host in ['example.com', 'test.com']:
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