from fastapi import FastAPI
import subprocess
class SanitizedCommand:
    def __init__(self, cmd):
        self.cmd = [c for c in cmd.split(' ') if c]
    def run(self):
        return subprocess.call(self.cmd)

app = FastAPI()
def sanitize_input(value):
    return ''.join(c for c in value if c.isalnum() or c in ' .,-')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    cmd = SanitizedCommand(f"ping {sanitized_host}")
    result = cmd.run()
    return {"status": "completed", "result": result}