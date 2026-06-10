from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

    def ping(self, host: str):
        command = self.ping_command + [shlex.quote(host)]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()
safe_pinger = SafePinger()

@app.get("/ping")
def ping(host: str):
    result = safe_pinger.ping(host)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }