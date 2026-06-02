from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate input to ensure it only contains allowed characters
        allowed_chars = set(char.isalnum() or char in '-.' for char in host)
        if all(allowed_chars):
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        else:
            raise ValueError('Invalid input')
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}