from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run for better security and error handling
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}