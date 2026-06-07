from fastapi import FastAPI
import subprocess
import shlex
class SafeCommand:
    def __init__(self, cmd: str):
        self.cmd = self._safe_command(cmd)

    def _safe_command(self, command: str) -> list:
        return shlex.split(command)

def ping(host: str):
    safe_cmd = SafeCommand(f'ping {host}')
    result = subprocess.run(safe_cmd.cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    return ping(host)