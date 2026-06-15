from fastapi import FastAPI
import subprocess
import shlex
class PingHandler:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> dict:
        try:
            result = await subprocess.run(shlex.split(f'ping {shlex.quote(self.host)}'), capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    handler = PingHandler(shlex.quote(host))  # Sanitize input here
    return handler.execute()