from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Sanitize the input to prevent command injection
        sanitized_host = subprocess.quote(self.host)
        return await asyncio.create_subprocess_exec('ping', sanitized_host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    result = await command.execute()
    output, error = await result.communicate()
    if error:
        return {'status': 'error', 'output': error.decode()}
    else:
        return {'status': 'completed', 'output': output.decode()}