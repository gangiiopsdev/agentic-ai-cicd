from fastapi import FastAPI
import subprocess
class SafeCommand:
    def __init__(self, cmd):
        self.cmd = cmd

    def run(self, *args):
        full_cmd = [self.cmd] + list(args)
        return subprocess.run(full_cmd, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_command = SafeCommand("ping")
    result = safe_command.run(host)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}