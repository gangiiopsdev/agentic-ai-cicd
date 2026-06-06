from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input to prevent command injection
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError("Invalid host")
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}