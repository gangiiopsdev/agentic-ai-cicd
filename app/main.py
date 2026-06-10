from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    host = subprocess.DEVNULL if host == '' else host
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class PingEndpoint:
    def __init__(self):
        self.app = FastAPI()
    @app.get("/ping")
    def ping(self, host: str):
        return {'status': 'completed', 'output': safe_ping(host)}