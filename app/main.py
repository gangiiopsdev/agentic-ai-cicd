from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        # Use shlex.quote to safely escape the user-provided input
        escaped_host = shlex.quote(host)
        subprocess.run(['ping', escaped_host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    PingService.safe_ping(host)
    return {"status": "completed"}