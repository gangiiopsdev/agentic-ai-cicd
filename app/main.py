from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command_parts):
    command = [shlex.quote(part) for part in command_parts]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f'Command failed: {e}')

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_subprocess_call(['ping', shlex.quote(host)])
    return {'status': 'completed'}