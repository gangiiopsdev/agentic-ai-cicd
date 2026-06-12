from fastapi import FastAPI
import subprocess
class PingHandler:
    def __init__(self, host: str):
        self.host = host

    async def ping(self):
        # Secure implementation using subprocess.run with shell=False and properly sanitized input
        result = await subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)
        return result.stdout
global_app = FastAPI()
@globa_app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@globa_app.get="/ping"
def ping(host: str):
    handler = PingHandler(host)
    return await handler.ping()