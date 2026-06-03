from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return result.stdout
class PingRouter:
    def __init__(self):
        self.app = FastAPI()
        self.register_routes()
    def register_routes(self):
        @self.app.get("/ping")
        async def ping(host: str):
            # Validate and sanitize the input to prevent command injection
            if not host.isalnum() or len(host) > 255:
                return {'status': 'error', 'message': 'Invalid host'}
            return {'status': 'completed', 'output': safe_ping(host)}
ping_router = PingRouter().app