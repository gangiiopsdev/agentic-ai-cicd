from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Validate and sanitize the host input
    try:
        result = subprocess.run(['ping', '-c', '4'] + shlex.split(host), capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}
    except Exception as e:
        raise ValueError('Invalid hostname or command execution failed')