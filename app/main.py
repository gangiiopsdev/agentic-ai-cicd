from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def execute_command(command, *args):
    if not all(re.match(r'^[a-zA-Z0-9.-]+$', arg) for arg in args):
        raise ValueError('Invalid arguments')
    return subprocess.run([command] + list(args), capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = execute_command('ping', host)
    return {'status': 'completed', 'output': result.stdout}