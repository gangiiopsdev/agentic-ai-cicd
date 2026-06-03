from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Validate and sanitize the input
        if not self.is_valid_host(self.host):
            raise ValueError('Invalid host')
        command = ['ping', self.host]
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE)
        return result.stdout.decode()[:100]

    def is_valid_host(self, host):
        import re
        pattern = r'^[a-zA-Z0-9.-]+$'
        return bool(re.match(pattern, host))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    result = await ping_command.execute()
    return {'status': 'completed', 'output': result[:100]}