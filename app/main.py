from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    sanitized_host = ''.join(filter(str.isalnum, host))
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
    return {'status': 'completed'}