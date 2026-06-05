from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    async def ping(self, host: str) -> dict:
        if not host.isnumeric() and ':' not in host:
            raise ValueError('Invalid host')
        try:
            result = await subprocess.run(['ping', '-c', '4', '--', f'"{host}"'], capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    return safe_pinger.ping(host)