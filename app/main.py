from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> str:
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stderr=subprocess.STDOUT, text=True)
            return await output.read()
        except subprocess.CalledProcessError as e:
            return f'Error: {e.output}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = await command.execute()
    return {'status': 'completed', 'result': result}