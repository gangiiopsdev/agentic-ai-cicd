from fastapi import FastAPI
import subprocess
c from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}