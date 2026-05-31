from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    async def ping(self, host: str) -> dict:
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')
        try:
            result = await subprocess.run(['ping', host], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    return safe_pinger.ping(host)