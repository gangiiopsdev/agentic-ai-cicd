from fastapi import FastAPI
import subprocess
import re
import shlex
def execute_command(command, *args):
    if not all(re.match(r'^[a-zA-Z0-9.-]+$', arg) for arg in args):
        raise ValueError('Invalid arguments')
    return subprocess.run([command] + list(map(shlex.quote, args)), capture_output=True, text=True, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = execute_command('ping', *map(shlex.quote, [host]))
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'message': str(e)}