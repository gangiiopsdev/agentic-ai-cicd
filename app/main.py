from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePing:
    def __init__(self):
        self.app = FastAPI()
    @app.get("/safe-ping")
    def safe_ping_route(self, host: str):
        return {'output': safe_ping(host)}