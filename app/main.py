from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self, host: str):
        self.host = host

    async def execute_ping(self) -> dict:
        args = ['ping', shlex.quote(self.host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_service = PingService(host)
    return ping_service.execute_ping()