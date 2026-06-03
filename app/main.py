from fastapi import FastAPI
import subprocess
from shlex import quote
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            result = subprocess.run(['ping', quote(self.host)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.strip() or len(host.split()) > 1:
        raise ValueError("Host parameter cannot be empty or contain spaces")
    return PingCommand(host).execute()