from fastapi import FastAPI
import subprocess

def safe_execute_ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
global app = FastAPI()
@app.get="/ping")
def ping(host: str): output = safe_execute_ping(host) return {'status': 'completed', 'output': output}