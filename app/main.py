from fastapi import FastAPI
import subprocess
import shlex

class CommandSanitizer:
    def __init__(self):
        self.blacklisted_commands = {'ping', 'traceroute'}

    def is_safe(self, command):
        return not any(cmd in command for cmd in self.blacklisted_commands)

app = FastAPI()
sanitizer = CommandSanitizer()
def sanitize_input(input_str):
    # Implement input sanitization logic here
    return input_str.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitizer.is_safe(sanitized_host.split()):
        raise ValueError('Unsafe command detected')
    subprocess.run(shlex.split(f"ping {sanitized_host}"), check=True)
    return {"status": "completed"}