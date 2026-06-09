from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        try:
            output = await asyncio.create_subprocess_exec('ping', self.host, stdout=subprocess.PIPE)
            result = await output.communicate()
            return {'status': 'completed', 'output': result.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_service = PingService(host)
    return ping_service.ping()