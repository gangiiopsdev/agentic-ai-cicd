from fastapi import FastAPI
import subprocess
class CommandSanitizer:
    def __init__(self, whitelist):
        self.whitelist = set(whitelist)

    def sanitize(self, command_str):
        return ' '.join([part for part in shlex.split(command_str) if any(part.startswith(prefix) for prefix in self.whitelist)])

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    whitelist = ['ping']  # Add other commands as needed
    sanitized_host = CommandSanitizer(whitelist).sanitize(host)
    command = ["ping", sanitized_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}