from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input to prevent command injection
    allowed_hosts = ['example.com', 'another-example.com']
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePing:
    def __init__(self):
        self.app = FastAPI()
    @app.get("/safe-ping")
    def safe_ping_route(self, host: str):  # Add input validation
        return {'output': safe_ping(host)}