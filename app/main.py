from fastapi import FastAPI
import subprocess
import shlex
import asyncio
import re

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        # Sanitize the host input to prevent command injection
        sanitized_host = re.sub(r'[^a-zA-Z0-9.-_]', '', host)
        try:
            command = ['ping', *shlex.split(sanitized_host)]
            result = await asyncio.to_thread(subprocess.run, command, capture_output=True, text=True, check=True)
            return {'status': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': f'Ping failed: {e}'}

safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        return {'status': 'Invalid host'}
    return safe_ping_instance.ping(host)