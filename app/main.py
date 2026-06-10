from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, command):
        self.command = shlex.split(command)

    def execute(self):
        return subprocess.run(self.command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_command = SafePing(f"ping {host}").execute()
    return {
        "status": "completed",
        "output": safe_command.stdout.decode() if safe_command.returncode == 0 else safe_command.stderr.decode()
    }