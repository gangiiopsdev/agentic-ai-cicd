from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> dict:
        try:
            result = await subprocess.run(['ping', self.host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler(host)
    return handler.execute()