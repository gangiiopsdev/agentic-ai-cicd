from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_execute(host: str):
        cmd = ['ping', host]
        subprocess.run(cmd, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    SafePing.safe_execute(host)
    return {"status": "completed"}