from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if host.strip().isdigit() and 1 <= int(host.strip()) <= 254:
        return host
    raise ValueError("Invalid host input")
class PingCommand:
    def __init__(self, host):
        self.host = validate_host(host)
    def run(self):
        command_parts = ['ping', '-c', '1', shlex.quote(self.host)]
        result = subprocess.run(command_parts, capture_output=True, text=True, check=False)
        return {"status": "completed", "output": result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str): 
    try:
        command = PingCommand(host)
        return command.run()
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}