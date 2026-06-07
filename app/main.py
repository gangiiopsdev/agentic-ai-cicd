from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            output = await asyncio.create_subprocess_exec('ping', host,
                                                           stdout=subprocess.PIPE,
                                                           stderr=subprocess.PIPE)
            stdout, stderr = await output.communicate()
            return {'status': 'completed', 'stdout': stdout.decode(), 'stderr': stderr.decode()}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)