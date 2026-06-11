from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    # Simple validation: allow only alphanumeric characters and a few special characters
    return all(c.isalnum() or c in '-.' for c in host)
class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    async def safe_ping(self, host: str) -> dict:
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid input'}
        try:
            args = shlex.split(f'{self.ping_command} {host}')
            result = subprocess.run(args, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping_instance.safe_ping(host)