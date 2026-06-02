from fastapi import FastAPI
import subprocess
import re
import shlex
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname format')
    try:
        result = subprocess.run(['ping', '-c', '4'] + shlex.split(host), capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'result': result.stdout}
    except Exception as e:
        raise ValueError('Invalid hostname or command execution failed')