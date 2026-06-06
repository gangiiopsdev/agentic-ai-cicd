from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_cmd = 'ping'

    def ping(self, host: str):
        args = [self.ping_cmd] + shlex.split(host)
        return subprocess.run(args)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    result = safe_ping_instance.ping(host)
    return {"status": "completed", "result": result}