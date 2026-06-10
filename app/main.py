from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    command = ' '.join(shlex.quote(part) for part in command_parts)
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent command injection
        raise ValueError('Invalid input')
    return run_command(['ping', host])