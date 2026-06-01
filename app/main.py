from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate input to ensure it only contains allowed characters (e.g., alphanumeric, dots, hyphens)
        if not all(c.isalnum() or c in '-.' for c in host):
            return {'status': 'failed', 'output': 'Invalid hostname'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}