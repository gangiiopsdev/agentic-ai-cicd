from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        # Safe implementation
        try:
            output = await self._ping_async(host)
            return {'status': 'completed', 'output': output}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

    async def _ping_async(self, host: str):
        import asyncio
        process = await asyncio.create_subprocess_exec('ping', host,
                                                        stdout=subprocess.PIPE,
                                                        stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return stdout.decode()

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    result = ping_service.ping(host)
    return result