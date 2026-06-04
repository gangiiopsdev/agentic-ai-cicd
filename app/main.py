from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize the input by removing potentially dangerous characters
        sanitized_host = ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))
        subprocess.run(['ping', sanitized_host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}