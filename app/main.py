from fastapi import FastAPI
import subprocess
from shlex import quote
def sanitize_input(user_input):
    return ''.join(filter(str.isalnum, user_input))

def run_safe_command(command_parts):
    safe_command = [os.path.abspath(cmd) for cmd in command_parts]
    subprocess.run(safe_command, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = quote(sanitize_input(host))
    run_safe_command(['ping', sanitized_host])
    return {'status': 'completed'}