from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.host = None

    def ping(self, host: str):
        self.host = host

app = FastAPI()
ping_service = SafePing()

@app.get("/ping")
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.call(args)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}