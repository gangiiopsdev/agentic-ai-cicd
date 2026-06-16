from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.trusted_hosts = {'localhost', '127.0.0.1'}

    async def ping(self, host: str):
        if host in self.trusted_hosts:
            try:
                result = await subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
                return {'status': 'completed', 'output': result.stdout}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': str(e)}
        else:
            return {'status': 'invalid_host'}

app = FastAPI()
safe_ping = SafePing()

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)