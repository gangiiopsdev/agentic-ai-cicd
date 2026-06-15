from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run and list
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}