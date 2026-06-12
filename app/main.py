from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize_command(command_parts):
        return [shlex.quote(part) for part in command_parts]

app = FastAPI()

def safe_subprocess(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    # Safe implementation with shlex.quote for input sanitization
    command_parts = ['ping', host]
    sanitized_command = CommandSanitizer.sanitize_command(command_parts)
    output = safe_subprocess(sanitized_command)
    if 'error' in output.lower():
        return {"status": "error", "message": output}
    return {"status": "completed", "output": output}