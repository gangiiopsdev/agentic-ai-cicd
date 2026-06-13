from fastapi import FastAPI
import subprocess
from html import escape
def sanitize_input(value: str) -> str:
    # Implement your sanitization logic here
    return escape(value)

class PingCommandSanitizer:
    def __init__(self, command_prefix=['ping']):
        self.command_prefix = command_prefix

    def sanitize_command(self, host: str):
        sanitized_host = ' '.join([item for item in self.command_prefix + [host.strip()] if item])
        return sanitized_host.strip()

app = FastAPI()
ping_sanitizer = PingCommandSanitizer()

@app.get("/ping")
def ping(host: str):
    command = ping_sanitizer.sanitize_command(host)
    try:
        result = subprocess.run(command.split(), check=True, capture_output=True, text=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}