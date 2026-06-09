from fastapi import FastAPI
import subprocess
import shlex
import os
def safe_exec(command, args):
    return ' '.join([command] + [shlex.quote(arg) for arg in args])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = 'ping'
    args = shlex.split(host)
    safe_command = safe_exec(command, args)
    if not any(os.path.exists(p) for p in [command] + args):
        return {'status': 'failed', 'error': 'Command not found'}
    try:
        output = subprocess.run(safe_command, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}