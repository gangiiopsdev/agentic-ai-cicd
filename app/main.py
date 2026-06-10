from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(host):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SecureFastAPI:
    def __init__(self):
        self.app = FastAPI()
    @app.get('/ping')
    def ping(self, host: str):
        return run_safe_command(host)
safe_app = SecureFastAPI().app