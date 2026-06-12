from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
class SafeSubprocess:
    @staticmethod
def run_command(command, args):
        try:
            output = subprocess.check_output([cmd_quote(command)] + [cmd_quote(arg) for arg in args], stderr=subprocess.STDOUT, universal_newlines=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_subprocess = SafeSubprocess()
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    # Ensure that the command does not contain shell metacharacters
    sanitized_host = cmd_quote(host)
    # Use `ping` without shell=True to prevent injection
    return safe_subprocess.run_command('ping', [sanitized_host])