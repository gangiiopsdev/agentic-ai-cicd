from fastapi import FastAPI
import subprocess
import shlex
class CommandLineSanitizer:
    @staticmethod
def sanitize_command(command_parts):
        return [shlex.quote(part) for part in command_parts]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    sanitized_host = CommandLineSanitizer.sanitize_command(['ping', host])
    subprocess.run(sanitized_host, check=True)
    return {'status': 'completed'}