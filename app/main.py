from fastapi import FastAPI
import subprocess
from shlex import quote

class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = quote(host)
        command = ["ping", safe_host]
        subprocess.call(command)
        return {"status": "completed"}

app = FastAPI()

@app.get("/ping")
def ping_wrapper(host: str):
    SafePing.ping(host)
    return {"status": "completed"}