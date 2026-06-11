from fastapi import FastAPI
import subprocess
class PingService:
    def __init__(self):
        self.valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._')

    async def is_valid_hostname(self, host: str) -> bool:
        return all(c in self.valid_chars for c in host)

app = FastAPI()
ping_service = PingService()

@app.get('/ping')
def ping(host: str):
    if not ping_service.is_valid_hostname(host):
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(['ping', '-c 1', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}