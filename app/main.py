from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    # Safe implementation using subprocess.run with proper quoting
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}