from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Safe implementation using list instead of string for subprocess arguments
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}