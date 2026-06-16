from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __call__(self, command_parts):
        try:
            result = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e.stderr)

app = FastAPI()

def ping(host: str):
    command_parts = ['ping', host]
    safe_ping = SafePing()
    output = safe_ping(command_parts)
    return {'status': 'completed', 'output': output}