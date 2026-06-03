from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', 'localhost']

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            return {'error': 'Invalid host'}
        try:
            await asyncio.create_subprocess_exec('ping', subprocess.check_output(['echo', host]).decode().strip())
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)