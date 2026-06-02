from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host or len(host) > 255 or any(c in host for c in [';', '&', '|', '>', '<', '*', '?', '~', '`', '{', '}', '[', ']', '\', '$', '#', '@', '^', '=', '+', ',', '.', '/', ':']):
        return {'status': 'failed', 'error': 'Invalid input'}
    command = PingCommand(host)
    return command.execute()

# Preventive controls:
# 1. Use a whitelist of allowed hosts.
# 2. Limit the length and format of the host input.
# 3. Avoid using subprocess for potentially dangerous commands.