from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

class PingService:
    def __init__(self):
        pass

    async def ping(self, host: str):
        try:
            result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode == 0:
                return JSONResponse(status_code=200, content={'status': 'completed', 'output': output.decode(), 'error': ''})
            else:
                return JSONResponse(status_code=400, content={'status': 'failed', 'error': error.decode() if error else 'Command failed'})
        except Exception as e:
            return JSONResponse(status_code=500, content={'status': 'failed', 'error': str(e)})

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)