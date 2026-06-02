from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.host = None

    def set_host(self, host: str):
        # Validate and sanitize input
        if isinstance(host, str) and host.strip().isalnum():
            self.host = host
        else:
            raise ValueError('Invalid host name')

app = FastAPI()

@app.get('/ping')
def ping(ping_command: PingCommand):
    # Fixed implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', ping_command.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}