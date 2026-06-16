from fastapi import FastAPI
import subprocess
import re
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self) -> bool:
        return re.match(r'^[a-zA-Z0-9.-]+$', self.host) is not None

    def run_command(self) -> dict:
        if not self.validate_host():
            return {'status': 'failed', 'error': 'Invalid input'}
        try:
            # Use shlex.quote to safely quote the host parameter
            quoted_host = shlex.quote(self.host)
            result = subprocess.run(['ping', quoted_host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return PingCommand(host).run_command()