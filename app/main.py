from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.hosts = ['127.0.0.1', '8.8.8.8']

    async def ping(self, host: str):
        if host in self.hosts:
            try:
                await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE)
                return {'status': 'completed'}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)