from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            if not host.isalnum():  # Basic input validation
                raise ValueError('Invalid host name')
            args = ['ping', host]  # Use list to avoid shell injection
            result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return str(e)

safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping_instance.ping(host)}