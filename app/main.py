from fastapi import FastAPI
import subprocess
import shlex
def run_safe_command(command_parts):
    try:
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Command failed: {e.stderr}'

class CommandSanitizer:
    @staticmethod
def sanitize_command(command_parts):
        sanitized_parts = [shlex.quote(part) for part in command_parts]
        return sanitized_parts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() and '-' not in host:
        return {'error': 'Invalid input'}, 400
    safe_command = CommandSanitizer.sanitize_command(['ping', host])
    return run_safe_command(safe_command)