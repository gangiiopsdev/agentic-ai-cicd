from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Input validation and sanitization
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}