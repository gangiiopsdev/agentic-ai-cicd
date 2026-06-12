from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'output': 'Invalid host'}
    ping_command = PingCommand(host)
    output = ping_command.execute()
    return {'status': 'completed', 'output': output}