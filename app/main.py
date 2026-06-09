from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        # Safe implementation using shlex for argument splitting
        try:
            subprocess.run(shlex.split(f"ping {host}"), check=True)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}
class PingApp(PingService):
    def __init__(self):
        super().__init__()
ping_app = PingApp()