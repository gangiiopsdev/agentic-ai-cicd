from fastapi import FastAPI
import shlex
import subprocess
import os

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            # Validate the input to prevent command injection
            if not all(c.isalnum() or c in '-.' for c in host):
                return {'status': 'Invalid hostname'}
            command = ['ping', *shlex.split(host)]
            result = await asyncio.to_thread(subprocess.run, command, capture_output=True, text=True, check=True)
            return {'status': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': f'Ping failed: {e}'}

safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)