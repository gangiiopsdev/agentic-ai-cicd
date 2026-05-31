from fastapi import FastAPI
import subprocess
from shlex import quote

class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', '-c', '1', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        SafePing.safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}