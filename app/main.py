from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Use shlex.quote to safely escape host input
    ping_command = ['ping', shlex.quote(host)]
    result = subprocess.run(ping_command, check=True, capture_output=True, text=True)
    return result.stdout

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/ping')
    def ping(self, host: str):
        try:
            output = safe_ping(host)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}

safe_ping_instance = SafePing()