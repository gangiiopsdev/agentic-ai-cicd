from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input before using it in the subprocess call
    sanitized_host = subprocess.quote(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}