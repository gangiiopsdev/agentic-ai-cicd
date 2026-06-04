from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum() and len(host) <= 64

@app.get('/ping')
def ping_route(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    command = PingCommand(host)
    return await command.execute()