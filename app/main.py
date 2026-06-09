from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        # Validate user input
        if not host or len(host) > 255 or not all(c.isalnum() or c in '.-\/' for c in host):
            return {"status": "failed", "error": "Invalid host"}
        
        try:
            args = shlex.split('ping ' + host)
            output = subprocess.run(args, capture_output=True, text=True, check=True)
            return {"status": "completed", "output": output.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
ping_service = PingService()