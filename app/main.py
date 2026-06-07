from fastapi import FastAPI
import subprocess
import shlex
import os
class SafePing:
    def __init__(self, host):
        self.host = host

    def validate_host(self):
        return os.path.basename(self.host) == self.host

    def execute_command(self):
        if not self.validate_host():
            raise ValueError('Invalid host')
        args = ['ping', shlex.quote(self.host)]  # Sanitize the input
        try:
            subprocess.run(args, check=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    result = safe_ping.execute_command()
    if isinstance(result, dict) and 'error' in result:
        return result
    else:
        return {'status': 'completed'}