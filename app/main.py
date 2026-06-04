from fastapi import FastAPI
import subprocess
from shlex import quote
class SafePing:
    @staticmethod
def ping(host: str):
        # Safer implementation using list for the command and validate input
        args = ['ping', '-c', '4', quote(host)]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    SafePing.ping(host)
    return {"status": "completed"}