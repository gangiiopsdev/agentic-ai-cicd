from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def safe_ping(host: str) -> None:
        # Use shlex.quote to safely escape the host parameter
        escaped_host = shlex.quote(host)
        subprocess.call(['ping', escaped_host], shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    PingService.safe_ping(host)
    return {"status": "completed"}