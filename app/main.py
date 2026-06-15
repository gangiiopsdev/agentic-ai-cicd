from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await subprocess.run(['ping', self.host], capture_output=True, text=True, timeout=5)
            return {'status': 'completed', 'result': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler(host)
    return handler.execute()