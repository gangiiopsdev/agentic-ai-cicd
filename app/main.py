from fastapi import FastAPI
import subprocess
from shlex import quote
class SafePing:
    @staticmethod
def safe_ping(host: str):
        args = ['ping', '--', host]
        subprocess.run(args, check=True, capture_output=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):    try:
        SafePing.safe_ping(quote(host))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}