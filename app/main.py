from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', 'localhost']

    async def ping(self, host: str) -> dict:
        if host not in self.allowed_hosts:
            return {'status': 'failed', 'error': 'Host is not allowed'}
        try:
            result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    if host not in safe_ping.allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}