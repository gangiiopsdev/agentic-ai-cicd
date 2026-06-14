from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def safe_ping(host: str) -> None:
        # Validate the host parameter
        if not all(c.isalnum() or c in '._-@' for c in host):
            raise ValueError("Invalid host")
        escaped_host = shlex.quote(host)
        subprocess.run(['ping', escaped_host], check=True, shell=False)
app = FastAPI()
@app.get="/ping")
def ping(host: str):
    PingService.safe_ping(host)
    return {"status": "completed"}