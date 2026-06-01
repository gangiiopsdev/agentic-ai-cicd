from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize the input
    host = subprocess.quote(host)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}