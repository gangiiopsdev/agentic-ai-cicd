from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping_host(self, host: str):
        args = ['ping', '-c', '1', host]
        result = await asyncio.create_subprocess_exec(*args,
                                                       stdout=subprocess.PIPE,
                                                       stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return output.decode(), error.decode()

app = FastAPI()

c ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    try:
        status, _ = ping_service.ping_host(host)
        return {'status': 'completed', 'result': status}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}