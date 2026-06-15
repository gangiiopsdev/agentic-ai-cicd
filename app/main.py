from fastapi import FastAPI
class PingService:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            result = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = await result.communicate()
            if result.returncode != 0:
                raise Exception(error.decode())
            return {'status': 'completed', 'output': output.decode()}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)