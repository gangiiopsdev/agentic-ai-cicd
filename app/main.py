from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize_command(command_parts):
        return [shlex.quote(part) for part in command_parts]
app = FastAPI()
def is_valid_host(host):
    # Basic validation, improve as needed
    if not host or ' ' in host:
        raise ValueError("Invalid host")
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    is_valid_host(host)
    command_parts = ['ping', host]
    sanitized_command = CommandSanitizer.sanitize_command(command_parts)
    subprocess.run(sanitized_command, check=True, capture_output=True, text=True)
    return {"status": "completed"}