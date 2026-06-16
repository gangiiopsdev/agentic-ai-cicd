from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping'}

    async def ping(self, host: str):
        if not any(host.startswith(cmd) for cmd in self.safe_commands):
            return {'status': 'failed', 'error': 'Invalid command'}
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping = SafePing()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)