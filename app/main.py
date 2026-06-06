from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        # Validate the host to ensure it's a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError('Invalid host provided')
        args = ['ping', self.host]
        try:
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e.stderr.strip()}'

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    return {'status': 'completed', 'output': command.execute()}