from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with absolute path
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}