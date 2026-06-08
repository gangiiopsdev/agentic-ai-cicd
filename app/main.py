from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)