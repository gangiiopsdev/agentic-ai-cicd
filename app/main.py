from fastapi import FastAPI
import os
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self) -> dict:
        if not self.is_safe_host():
            return {'status': 'error', 'message': 'Invalid host'}

        cmd = ['ping', '-c', '1', self.host]
        try:
            result = await os.run_async(cmd, capture_output=True, timeout=5)
            return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}

    def is_safe_host(self) -> bool:
        # Implement logic to validate the host to prevent command injection
        allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
        return self.host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    return ping_command.execute()