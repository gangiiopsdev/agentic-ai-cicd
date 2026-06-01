from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.pings = {'google.com': None}

    async def ping(self, host: str):
        if host not in self.pings:
            return {'status': 'failed', 'error': 'Host not allowed'}
        try:
            subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
            return {'status': 'success', 'output': subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True).stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    return ping_service.ping(host)