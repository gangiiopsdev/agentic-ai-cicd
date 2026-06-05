from fastapi import FastAPI
import subprocess
import shlex
class CommandSanitizer:
    @staticmethod
def sanitize(command: str) -> str:
        return ' '.join(shlex.quote(arg) for arg in command.split())

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run([CommandSanitizer.sanitize('ping'), CommandSanitizer.sanitize(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}