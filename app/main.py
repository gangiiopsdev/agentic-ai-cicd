from fastapi import FastAPI
import shlex
import subprocess

def safe_ping(host: str):
    # Sanitize the input to avoid shell injection
    host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

class PingRouter:
    def __init__(self):
        self.app = FastAPI()
        self.register_routes()

    def register_routes(self):
        @self.app.get("/ping")
        async def ping(host: str):
            return {'status': 'completed', 'output': safe_ping(host)}
ping_router = PingRouter().app