from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    async def execute(self):
        try:
            result = await subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isdigit() and '@' not in host:
        return {'status': 'error', 'message': 'Invalid host'}
    ping_command = PingCommand(host)
    return await ping_command.execute()