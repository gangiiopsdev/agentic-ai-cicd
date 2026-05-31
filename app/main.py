from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['localhost', '127.0.0.1']

    async def ping(self, host: str) -> bool:
        if host not in self.allowed_hosts:
            return False
        subprocess.call(f'ping {host}', shell=False)
        return True

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    result = safe_ping.ping(host)
    if result:
        return {'status': 'completed'}
    else:
        return {'error': 'Host not allowed'}, 403