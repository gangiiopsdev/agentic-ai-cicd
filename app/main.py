from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'example.com', 'localhost'}

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Host not allowed')
        # Safe implementation
        subprocess.call(['ping', host])
        return {'status': 'completed'}

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)