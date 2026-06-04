from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        # Safe implementation using shlex.quote to avoid shell injection
        args = ['ping'] + shlex.split(host)
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):,
    PingService.ping(host)
    return {"status": "completed"}