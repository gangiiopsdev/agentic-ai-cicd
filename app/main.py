from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        try:
            # Validate input to ensure it does not contain malicious commands
            if any(char in host for char in [';', '|', '&', '*', '?', '<', '>', '\', '`', '$']):
                return {"error": "Invalid input detected"}
            subprocess.run(shlex.split(f"ping {host} --wait=1"), check=True, shell=False)
            return {"status": "completed"}
        except subprocess.CalledProcessError as e:
            return {"error": str(e)}
class PingApp(PingService):
    def __init__(self):
        super().__init__()
ping_app = PingApp()