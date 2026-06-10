from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = subprocess.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}