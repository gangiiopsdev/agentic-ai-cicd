from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = shlex.quote(host)
        subprocess.call(['ping', safe_host])
app = FastAPI()
@app.get("/ping")
def ping_safe(host: str):
    SafePing.ping(host)
    return {"status": "completed"}