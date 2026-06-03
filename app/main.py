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
    # Use a whitelist of allowed hosts and limit the length and format of the host input.
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    if not host or len(host) > 255 or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid input'}
    command = PingCommand(host)
    return command.execute()

# Preventive controls:
# 1. Use a whitelist of allowed hosts.
# 2. Limit the length and format of the host input.