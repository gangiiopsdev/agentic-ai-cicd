from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        args = shlex.split(f'ping {shlex.quote(host)}')
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    PingService.safe_ping(host)
    return {"status": "completed"}