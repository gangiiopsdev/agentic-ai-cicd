from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}