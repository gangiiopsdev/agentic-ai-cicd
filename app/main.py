from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = ['ping']

    def run(self, host):
        args = self.ping_command + shlex.split(host)
        subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.run(host)
    return {"status": "completed"}