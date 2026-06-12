from fastapi import FastAPI
import subprocess
def run_safe_command(host):
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to escape special characters
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SecureFastAPI:
    def __init__(self):
        self.app = FastAPI()
    @app.get('/ping')
    def ping(self, host: str):
        if not all(c.isalnum() or c in ' .-[]{}()=' for c in host):  # Basic validation of the input
            raise ValueError('Invalid host name')
        return run_safe_command(host)
safe_app = SecureFastAPI().app