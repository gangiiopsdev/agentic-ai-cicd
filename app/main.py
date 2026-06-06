from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    safe_input = ''.join(c for c in user_input if c.isalnum() or c in ('.', '-', '_'))
    return safe_input
def execute_safe_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, text=True, timeout=5)
        return result.stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return str(e)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    output = execute_safe_command('ping', '-c 1', safe_host)
    return {'status': 'completed' if output else 'failed', 'output': output}