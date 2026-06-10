from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def __init__(self):
        self.app = FastAPI()

    @app.get("/ping")
    async def ping(self, host: str):
        if not host or not host.isalnum():
            return {"status": "invalid host"}
        command = shlex.split(f'ping {host}')
        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {
                "status": "completed",
                "output": result.stdout.decode()
            }
        except subprocess.CalledProcessError as e:
            return {
                "status": "error",
                "message": str(e),
                "stdout": e.stdout.decode(),
                "stderr": e.stderr.decode()
            }

# Usage
ping_service = PingService()
ping_service.app.include_router(ping_service.app.router)