from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    async def ping(self, host: str):
        if not self.is_safe_host(host):
            return {'status': 'error', 'message': 'Unsafe host'}
        command = ['ping', host]
        subprocess.call(command)

    def is_safe_host(self, host: str):
        # Implement safe host validation logic here
        return True if host == 'example.com' else False

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):\n    return await safe_ping.ping(host)\n