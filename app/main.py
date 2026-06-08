from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        try:
            # Secure implementation using subprocess.run with shell=False and args parameter
            await asyncio.create_subprocess_exec('ping', self.host)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler(host)
    result = handler.execute()
    return await result