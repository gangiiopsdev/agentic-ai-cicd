from fastapi import FastAPI
import subprocess
import re

class SafePing:
    def __init__(self, host):
        self.host = host

    async def run(self):
        # Validate the host input to prevent injection attacks
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError('Invalid host name')
        try:
            result = await asyncio.create_subprocess_exec('ping', self.host, check=True, capture_output=True, text=True)
            return {'host': self.host, 'result': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'host': self.host, 'error': e.stderr}

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    safe_ping_instance = SafePing(host)
    return await safe_ping_instance.run()