from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return output.decode('utf-8'), error.decode('utf-8')
        except Exception as e:
            return str(e), None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host name'}
    ping_command = PingCommand(host)
    output, error = await ping_command.execute()
    if error:
        return {'status': 'failed', 'error': error}
    return {'status': 'completed', 'output': output}