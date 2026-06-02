from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Sanitize the input to prevent injection
        host = subprocess.quote(host)
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}