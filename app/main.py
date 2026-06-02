from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        self.ping_command = 'ping'

    async def safe_ping(self, host: str):
        if not host or not host.strip():
            raise ValueError('Host cannot be empty')
        args = [self.ping_command] + shlex.split(host)
        result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping(host: str):
    return ping_service.safe_ping(host)