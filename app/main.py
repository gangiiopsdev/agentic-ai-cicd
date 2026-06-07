from fastapi import FastAPI
import subprocess
from shlex import quote
class CommandRunner:
    def __init__(self, host):
        self.host = host

    async def run(self):
        cmd = ['ping', quote(self.host)]
        result = await asyncio.create_subprocess_exec(*cmd,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
        return await result.communicate()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    runner = CommandRunner(host)
    output, error = runner.run()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode() if error else None}
def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts