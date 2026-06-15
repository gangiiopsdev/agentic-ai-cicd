from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.sanitized_commands = {
            'google.com': True,
            '127.0.0.1': True
        }

    async def ping(self, host: str):
        if host not in self.sanitized_commands:
            return {'status': 'Invalid host'}
        subprocess.call(['ping', host])

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)