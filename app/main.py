from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess(command, **kwargs):
    # Use shlex to safely split the command into a list of arguments
    args = shlex.split(command)
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True, **kwargs)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

app = FastAPI()

def ping(host: str):
    # Secure implementation using safe_subprocess
    if not host.isalnum():
        return {'status': 'error', 'error': 'Invalid input'}
    command = f'ping {host}'
    return safe_subprocess(command)