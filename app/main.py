from fastapi import FastAPI
import subprocess
import shlex
import re

def validate_host(host):
    if not host.strip().isdigit() or len(host) > 3:
        raise ValueError("Invalid host input")
    return host

class PingCommand:
    def __init__(self, host):
        self.host = validate_host(host)

    def run(self):
        args = ['ping', str(self.host)]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            return {"status": "failed", "error": result.stderr}
        return {"status": "completed", "output": result.stdout}

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        command = PingCommand(host)
        return command.run()
    except Exception as e:
        return {"status": "failed", "error": str(e)}