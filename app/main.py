from fastapi import FastAPI
import subprocess
import shlex
import asyncio

class PingService:
    @staticmethod
    async def safe_ping(host: str) -> (bool, str):
        try:
            args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
            result = await asyncio.create_subprocess_exec(*args, check=True, capture_output=True, text=True)
            return True, result.stdout.decode()
        except subprocess.CalledProcessError as e:
            return False, str(e)

app = FastAPI()
ping_service = PingService()

@app.get("/ping")
def ping(host: str):
    success, output = ping_service.safe_ping(host)
    if not success:
        return {"status": "failed", "message": "Invalid host", "output": output}
    return {"status": "completed", "output": output}