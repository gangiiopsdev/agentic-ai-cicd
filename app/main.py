from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using absolute path to avoid command injection
        result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}