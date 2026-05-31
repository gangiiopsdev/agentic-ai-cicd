from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    async def ping(self, host: str):
        try:
            command = ['ping', *shlex.split(host)]
            result = await asyncio.to_thread(subprocess.run, command, capture_output=True, text=True, check=True)
            return {'status': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': f'Ping failed: {e}'}

safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)