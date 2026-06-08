from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.app = FastAPI()

    def safe_ping(self, host: str):
        # Safe implementation using shlex.quote to escape arguments
        subprocess.call(shlex.split(f"ping {shlex.quote(host)}"))

    @app.get("/ping")
    async def ping(self, host: str):
        self.safe_ping(host)
        return {"status": "completed"}

safe_ping_instance = SafePing()