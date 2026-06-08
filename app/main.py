from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    def __init__(self, whitelist):
        self.whitelist = set(whitelist)

    def sanitize(self, command_str):
        command_parts = shlex.split(command_str)
        sanitized_parts = [part for part in command_parts if any(part.startswith(prefix) for prefix in self.whitelist)]
        return ' '.join(sanitized_parts)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    whitelist = ['ping']  # Add other commands as needed
    sanitized_host = CommandSanitizer(whitelist).sanitize(host)
    command = f"ping {shlex.quote(sanitized_host)}"
    result = subprocess.run(command, shell=False, check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode() if not result.stderr else result.stderr.decode()}