from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Safe implementation using subprocess.run with a list of arguments
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}