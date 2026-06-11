from fastapi import FastAPI
import asyncio
import re
import subprocess

class PingCommand:
    def __init__(self):
        self.command = ['ping', '-c', '1']

    async def run(self, host: str):
        # Validate input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host.strip()) == 0:
            return {'status': 'error', 'stderr': 'Invalid host name'}
        try:
            result = await asyncio.to_thread(subprocess.run, self.command + [host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'stderr': e.stderr.decode()}

app = FastAPI()
cmd = PingCommand()
@app.get("/ping")
def ping_route(host: str):
    return cmd.run(host)