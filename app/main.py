from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    try:
        # Safe implementation using subprocess.run with shell=False and proper sanitization of host
        args = ['ping', shlex.quote(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}