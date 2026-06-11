from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(host):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout
class SecureFastAPI:
    def __init__(self):
        self.app = FastAPI()
    @app.get('/ping')
    def ping(self, host: str):
        try:
            return run_safe_command(host)
        except subprocess.CalledProcessError as e:
            return {'error': 'Command failed', 'output': e.stderr}
safe_app = SecureFastAPI().app