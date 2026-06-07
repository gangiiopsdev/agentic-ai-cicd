from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Validate the host input to ensure it's safe to use in a command
        host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}