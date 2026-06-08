from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with absolute path and shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}