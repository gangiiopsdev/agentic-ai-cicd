from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}