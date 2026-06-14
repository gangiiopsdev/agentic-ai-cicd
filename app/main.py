from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        command = shlex.split(f'ping {shlex.quote(self.host)}')
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return e.stderr

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    output = safe_ping.ping()
    return {"status": "completed", "output": output}